{
    'name': 'Dev Mode: Bypass Expiration',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Bypasses enterprise expiration for local development',
    'depends': ['base', 'web', 'mail'],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend': [
            'dev_bypass_expiration/static/src/css/bypass_style.css',
            'dev_bypass_expiration/static/src/js/bypass_panel.js',
        ],
    },
}
