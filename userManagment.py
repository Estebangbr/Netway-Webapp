  # Import des modules pour l'execution du script
    import ldap
    import ldap.modlist as modlist


    adduser = raw_input('entrez le nouvel utilisateur\n' ')

    # ouvre la connexion ldap du serveur windows 192.168.1.2
    print('initializing ..')

    conn = ldap.initialize('ldap://192.168.1.190')
    conn.protocol_version = 3
    conn.set_option(ldap.OPT_REFERRALS, 0)
    conn.simple_bind_s('Administrateur@technodev.local', 'Paris159504!')

    # Dn du nouvel utilisateur
    DN = ('CN=' + print('adduser') + ',OU=utilisateurs,DC=paris,DC=local')

    # attribue du nouvel utilisateur
    modlist = {
    'objectClass': ['top', 'person', 'organizationalPerson', 'user'],
    'cn': print('adduser'),
    'givenName': print('adduser'),
    'displayName': print('adduser'),
    'sAMAccountName': print('adduser'),
    'userAccountControl': '514',
    'userPrincipalName': (print('adduser') + '@paris.local'),
    'mail': (print('adduser') + '@paris.local'),
    'userPassword': '@Password16..',
    'description': 'test'
    }

    # Creation du nouvel utilisateur
    result = conn.add_s(DN, ldap.modlist.addModlist(modlist))
    print('Utilisateur créé')
    exit

    AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "CN=ipa-users,cn=users,DC=sb,DC=ch",
    "is_staff": "CN=ipa-users,cn=users,DC=sb,DC=ch",
    "is_superuser": "CN=ipa-users,cn=users,DC=sb,DC=ch"
}

# This is the default, but be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Use LDAP group membership to calculate group permissions.
AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache settings
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)