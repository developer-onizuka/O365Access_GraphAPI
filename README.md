# O365Access_GraphAPI


# 1. Create Developer Account (Free)
> https://developer.microsoft.com/ja-jp/microsoft-365/dev-program

Confirm the link below, and you can see "Microsoft 365 E5 Developer" in subscription.
> https://portal.office.com/account/?ref=MeControl#subscriptions

# 2. Create App in Azure AD
Login to [Azure](https://portal.azure.com).

# 2-1. App registrations
(1) Select "App registrations" in Azure portal's Blade <br>
(2) Select "New registration" in App registraitons's tab <br>
(3) Enter the App name in the name box <br>
    ex: getMail, getPresence, etc <br>
(4) Enter redirect URI <br>
    ex: http://localhost/ <br>
(5) Select Register button underneath <br>
(6) Check Client ID and Tenant ID <br>

# 2-2. Create client secrets
(7) Select "Certificates & Secrets" in the registered App's Blade <br>
(8) Create the secret <br>
(9) Copy it to a text file, temporary <br>

# 2-3. Grant Read permission

