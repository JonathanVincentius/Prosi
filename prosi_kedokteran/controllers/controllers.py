from odoo import http
from odoo.http import request

class ProsiKedokteranPages(http.Controller):

    
    # 1. HALAMAN UTAMA (WELCOME PAGE)
    
    @http.route('/kedokteran', type='http', auth='public', website=True)
    def welcome_page(self, **kw):
        """Menampilkan halaman awal BandaSehat"""
        return request.render('prosi_kedokteran.custom_welcome_template', {})

    
    # 2. HALAMAN LOGIN KUSTOM
    
    @http.route('/kedokteran/login', type='http', auth='public', website=True)
    def custom_login_page(self, **kw):
        """Menampilkan form login kustom dari file login.xml"""
        return request.render('prosi_kedokteran.custom_login_template', {})

    
    # 3. HALAMAN REGISTRASI KUSTOM
    
    @http.route('/kedokteran/register', type='http', auth='public', website=True)
    def custom_register_page(self, **kw):
        """Menampilkan form pendaftaran akun baru dari file register.xml"""
        return request.render('prosi_kedokteran.custom_register_template', {})