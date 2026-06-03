from odoo import models, fields, api

class UsersIbu(models.Model):
    _name = 'users.ibu'
    _description = 'Data Profil Ibu dan Anak'
    _table = 'users_ibu'  # Mengunci nama tabel di database menjadi users_ibu

    # Menghubungkan (mendelegasikan) model ini ke res.users bawaan Odoo
    _inherits = {'res.users': 'user_id'}

    # Field penghubung wajib (Foreign Key)
    user_id = fields.Many2one(
        'res.users', 
        string='User Odoo Terkait', 
        required=True, 
        ondelete='cascade'
    )

    # Field Kustom Riwayat Obstetri
    count_pregnancy = fields.Integer(string='Jumlah Kehamilan', default=0)
    count_birth = fields.Integer(string='Jumlah Melahirkan', default=0)
    count_miscarriage = fields.Integer(string='Jumlah Keguguran', default=0)

    # Field Kustom Fase Konten Ibu
    fase_ibu = fields.Selection([
        ('pra', 'Pra-Kehamilan'),
        ('hamil', 'Sedang Hamil'),
        ('bayi', 'Punya Bayi')
    ], string='Fase Ibu', default='hamil', required=True)

    birth_date_custom = fields.Date(string='Tanggal Lahir Bunda')
