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