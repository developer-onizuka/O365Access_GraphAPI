# O365Access_GraphAPI


# 1. Create Developer Account (Free)
> https://developer.microsoft.com/ja-jp/microsoft-365/dev-program

Confirm the link below, and you can see "Microsoft 365 E5 Developer" in subscription.
> https://portal.office.com/account/?ref=MeControl#subscriptions

# 2. Create App in Azure AD
Login to [Azure](https://portal.azure.com).

# 2-1. App registrations
(1) Select "App registrations" in Azure portal's Blade
(2) Select "New registration" in App registraitons's tab
(3) Enter the App name in the name box
    ex: getMail, getPresence, etc
(4) Enter redirect URI
    ex: http://localhost/
(5) Select Register button underneath
(6) Check Client ID and Tenant ID

# 2-2. Create client secrets
(7) Select "Certificates & Secrets" in the registered App's Blade
(8) Create the secret
(9) Copy it to a text file, temporary

# 2-3. Grant Read permission

