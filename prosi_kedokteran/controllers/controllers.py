from odoo import http
from odoo.http import request

class ProsiKedokteranWeb(http.Controller):

    # 1. Halaman Login Kustom
    @http.route('/kedokteran/login', type='http', auth='public', website=True)
    def custom_login_page(self, **kw):
        # Mengembalikan template HTML kustom kita sendiri
        return request.render('prosi_kedokteran.custom_login_template', {})

    # 2. Endpoint untuk memproses Data Login (Form Post)
    @http.route('/kedokteran/login/submit', type='http', auth='public', methods=['POST'], csrf=False)
    def custom_login_submit(self, **kw):
        username = kw.get('login')
        password = kw.get('password')
        
        try:
            # Melakukan autentikasi ke database Odoo secara backend
            uid = request.session.authenticate(request.db, username, password)
            if uid:
                # Jika sukses, arahkan ke halaman utama buatan sendiri
                return request.redirect('/kedokteran/dashboard')
        except Exception:
            return "Login Gagal! Username atau Password Salah."