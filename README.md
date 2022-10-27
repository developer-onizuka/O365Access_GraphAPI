# O365Access_GraphAPI

Microsoft Graph is the gateway to data and intelligence in Microsoft 365. It provides a unified programmability model that you can use to access the tremendous amount of data in Microsoft 365, Windows, and Enterprise Mobility + Security. Use the wealth of data in Microsoft Graph to build apps for organizations and consumers that interact with millions of users.

![O365Access_GraphAPI.png](https://github.com/developer-onizuka/Diagrams/blob/main/O365Access_GraphAPI/O365Access_GraphAPI.drawio.png)

# 1. Create Developer Account
You can create Developer Account as free so that you can test your O365 app.
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
(4) Enter redirect URI (**Very carefully you need "/" at the end.**)<br>
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
(13) Select "Application permissions" for Client Credentials Flow or "Delegated permissions" for Implicit Credentials Flow. <br>
(14) Select the permission to let grant
```
     ex: Mail.Read
```
(15) Click "Grant admin consent for App" in API permission's tab (**Important**) <br>
(16) Check if API/Permisson is granted (See status row)

# 2-4. Implicit credentials flow 
**If you select Delegated permissions, then it might be not neccessary.**<br>
(17) Select "Authentication" in the registered App's Blade <br>
(18) Select "Access tokens" and "ID tokens" <br>
(19) Save it

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
As you can see below, the resource owner(=you) will not be involved during Client Credentials Flow. It means only going through between WebApp and AzureAD not involving the resource owner, so it is also called as **2-legged OAuth**.

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
Enter the URL into your browser. You don't need to specify the CLIENT_CECRET in it because you're asked the consent by AzureAD through browser, soon. <br> **What is the defference between Implicit Credentials Flow and Client Credentials Flow is:** <br>
**Implicit Credentials** : On behalf of users (**act as the signed-in user**) <br>
**Client Credentials**   : 2-legged OAuth (**run without a signed-in user present, for example, apps that run as background services or daemons**) <br>
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
  ...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 23199    0 23199    0     0   112k      0 --:--:-- --:--:-- --:--:--  112k
"You've joined the Sample Team Site group"
```

See also [Microsoft Graph REST API v1.0 endpoint reference](https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0). <br>

# 5-4. Other APIs
You add the scope=https://graph.microsoft.com/Presence.Read.All in addition to above. You can use "%20" which means space.
```
&scope=https://graph.microsoft.com/Mail.Read%20https://graph.microsoft.com/Presence.Read.All
```
Before login to Teams App.
```
# curl -H "Authorization: Bearer xxx..." https://graph.microsoft.com/v1.0/me/presence |jq .availability
  ...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   220    0   220    0     0   2178      0 --:--:-- --:--:-- --:--:--  2178
"Offline"
```

After login to Teams App.
```
# curl -H "Authorization: Bearer xxx..." https://graph.microsoft.com/v1.0/me/presence |jq .availability
  ...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   220    0   220    0     0   2178      0 --:--:-- --:--:-- --:--:--  2178
"Available"
```

# 6. Reference
> https://dev.classmethod.jp/articles/microsoft-graph-python/<br>
> https://ashiqf.com/2021/03/16/call-microsoft-graph-api-as-a-signed-in-user-with-delegated-permission-in-power-automate-or-azure-logic-apps-using-http-connector/<br>
> https://qiita.com/massie_g/items/fe7540161aa4a5f86bf5<br>
