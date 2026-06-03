from odoo import http
from odoo.http import request

class ProsiKedokteranWeb(http.Controller):

    
    # 1. HALAMAN LOGIN 
    
    @http.route('/kedokteran/login', type='http', auth='public', website=True)
    def custom_login_page(self, **kw):
        """Menampilkan form login kustom dari file login.xml"""
        return request.render('prosi_kedokteran.custom_login_template', {})

    
    # 2. PROSES SUBMIT FORM LOGIN
    
    @http.route('/kedokteran/login/submit', type='http', auth='public', methods=['POST'], csrf=False)
    def custom_login_submit(self, **kw):
        """Memproses data username & password yang dikirim dari form login"""
        username = kw.get('login')
        password = kw.get('password')
        
        try:
            # Melakukan autentikasi ke database Odoo
            uid = request.session.authenticate(request.db, username, password)
            if uid:
                # Jika sukses, arahkan ke halaman dashboard kustom (akan kita buat nanti)
                return request.redirect('/kedokteran/dashboard')
        except Exception:
            # Jika salah username/password atau error lainnya
            return "<h3>Login Gagal! Username atau Password Salah.</h3><br/><a href='/kedokteran/login'>Kembali ke Login</a>"


    # 3. HALAMAN REGISTRASI KUSTOM
    
    @http.route('/kedokteran/register', type='http', auth='public', website=True)
    def custom_register_page(self, **kw):
        """Menampilkan form pendaftaran pasien/user baru dari file register.xml"""
        return request.render('prosi_kedokteran.custom_register_template', {})