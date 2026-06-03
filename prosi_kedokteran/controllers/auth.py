from odoo import http
from odoo.http import request

class ProsiKedokteranAuth(http.Controller):

    @http.route('/kedokteran/login/submit', type='http', auth='public', methods=['POST'], csrf=False)
    def custom_login_submit(self, **kw):

        username = kw.get('login')
        password = kw.get('password')

        try:
            uid = request.session.authenticate(
                request.env.cr.dbname,
                {
                    'login': username,
                    'password': password,
                    'type': 'password'
                }
            )

            if uid:
                return request.redirect('/kedokteran')

        except Exception:
            pass

        return request.redirect('/kedokteran/login')

    # ==========================================
    # 2. PROSES SUBMIT FORM REGISTRASI (TANPA OTOMATIS LOGIN)
    # ==========================================
    @http.route('/kedokteran/register/submit', type='http', auth='public', methods=['POST'], csrf=False)
    def custom_register_submit(self, **kw):
        """Menangkap input dari register.xml, menyimpan ke database, lalu melempar ke halaman login"""
        
        # Ambil data dasar login
        name = kw.get('name')
        login = kw.get('login')      
        password = kw.get('password')
        
        # Ambil data tambahan profil kustom
        phone = kw.get('phone', '')
        address = kw.get('address', '')
        fase = kw.get('fase', 'hamil') 
        
        # Format Tanggal Lahir kustom
        b_date = kw.get('birth_date', '')
        b_month = kw.get('birth_month', '')
        b_year = kw.get('birth_year', '')
        birth_date_string = f"{b_year}-{b_month}-{b_date}" if b_year and b_month and b_date else False

        if not name or not login or not password:
            return "<h3>Registrasi Gagal! Nama, Username, dan Password wajib diisi.</h3><br/><a href='/kedokteran/register'>Kembali</a>"

        try:
            # Akses pool model kustom users.ibu
            ibu_sudopool = request.env['users.ibu'].sudo()
            
            # Validasi duplikasi username ke res.users bawaan
            existing_user = request.env['res.users'].sudo().search([('login', '=', login)])
            if existing_user:
                return "<h3>Registrasi Gagal! Username sudah digunakan oleh Bunda lain.</h3><br/><a href='/kedokteran/register'>Coba Username Lain</a>"

            # Simpan data ke database 
            new_ibu_record = ibu_sudopool.create({
                # Field Delegasi dari res.users
                'name': name,
                'login': login,
                'password': password,
                'phone': phone,
                'street': address,
                
                # Field Murni dari tabel users_ibu
                'count_pregnancy': int(kw.get('count_pregnancy') or 0),
                'count_birth': int(kw.get('count_birth') or 0),
                'count_miscarriage': int(kw.get('count_miscarriage') or 0),
                'fase_ibu': fase,
                'birth_date_custom': birth_date_string if birth_date_string else False
            })

            
            # tanpa butuh konfirmasi email / token signup dari Odoo core
            new_user_partner = new_ibu_record.user_id
            new_user_partner.write({'active': True})

            # Alihkan langsung secara bersih ke halaman login kustom Anda
            # Anda juga bisa menambahkan pesan sukses via parameter URL jika mau
            return request.redirect('/kedokteran/login?signup_success=1')

        except Exception as e:
            return f"<h3>Terjadi kesalahan saat mendaftar:</h3><p>{str(e)}</p><br/><a href='/kedokteran/register'>Kembali ke Form</a>"