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
```
    ex: getMail, getPresence, etc
```
(4) Enter redirect URI <br>
```
    ex: http://localhost/
```
(5) Select Register button underneath <br>
(6) Check Client ID and Tenant ID <br>

# 2-2. Create client secrets
(7) Select "Certificates & Secrets" in the registered App's Blade <br>
(8) Create the secret <br>
(9) Copy it to a text file, temporary <br>

# 2-3. Grant Read permission
(10) Select "API permissions" in the registered App's Blade <br>
(11) Select "Add a permission" in API permissions's tab <br>
(12) Select "Microsoft Graph" in a poped-up window <br>
(13) Select the permission to let grant
```
     ex: Mail.Read
```
(14) Click "Grant admin consent for App" in API permission's tab (**Important**) <br>
(15) Check if API/Permisson is granted (See status row)

# 2-4. Implicit credentials flow (for Step5)
(16) Select "Authentication" in the registered App's Blade <br>
(17) Select "Access tokens" and "ID tokens" <br>
(18) Save it

# 3. Create VM for Python
```
# git clone https://github.com/developer-onizuka/O365Access_GraphAPI
# cd O365Access_GraphAPI
# vagrant up --provider=libvirt
# vagrant ssh
```
```
# pip install msal
```

