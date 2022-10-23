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

# 4. Get Mail from O365 with Client Credentials Flow
```
# export TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
# export CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
# export CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# export USER_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```
```
# git clone https://github.com/developer-onizuka/O365Access_GraphAPI
# cd O365Access_GraphAPI
```
You can find mail as followings:
```
# python3 getMail.py 
New access token retrieved....
2022-10-15T11:54:24Z ----- subject: You've joined the Sample Team Site group
```

# 5. Get Mail from O365 with Implicit Credentials Flow

# 5-1. Token Request to AzureAD
Enter the URL into your browser. You don't need to specify the CLIENT_CECRET in it because you're asked the consent by AzureAD through browser, soon.
```
https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/authorize
?client_id=<CLIENT_ID>
&response_type=token
&redirect_uri=http://localhost/
&scope=https://graph.microsoft.com/Mail.Read
```

# 5-2. Response in browser's address bar
The response in the address bar contains "**access_token**". You copy and use it to access to O365's Graph API.

http://localhost/
**#access_token=xxx...**
&token_type=Bearer
&expires_in=3971
&scope=profile+openid+email+https%3a%2f%2fgraph.microsoft.com%2fMail.Read
&session_state=xxx...

# 5-3. Access to O365's Graph API with token
You can put the token retrieved into the header of API call. You can find messages.
```
# curl -H "Authorization: Bearer xxx..." https://graph.microsoft.com/v1.0/me/messages |jq .value[].subject

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 23199    0 23199    0     0   112k      0 --:--:-- --:--:-- --:--:--  112k
"You've joined the Sample Team Site group"
```

See also [Microsoft Graph REST API v1.0 endpoint reference](https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0). <br>

# 5-4. Other APIs


