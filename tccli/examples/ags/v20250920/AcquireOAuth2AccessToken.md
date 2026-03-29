**Example 1: 查询 session 状态**



Input: 

```
tccli ags AcquireOAuth2AccessToken --cli-unfold-argument  \
    --WorkloadIdentityToken eyJ**************************************c*******Y*************************************Zpbm9mbGl1YXZjIiwiYXVkIjpbInNhbmR********************iOjE3NzQ***************I*******Q1MjY1NiwianRpIjoiZTc1M2VjOTAtMDY2YS00ZWZiLWJk****Mjc4ZjUwNmM4YzA***********xvY***aWRlbnRpdHlfaWQiOiJ3aS0wMzA5YTViOSIsInV*************************Yy**************************NZID4**************************SElAxJ-kk9gB7Qu94seH8n4fm66_2wVLxIJp**********Y**U*****8IdGhdPm********c**h**L****c*****VcZdbsm-RI***_***********m1zQn0o**********************kcxvzQvCfft***u********xxZu5vDYtsrbsxQv********r******QO_Za3wQADjNAj*******************u6Zea8ywK******************kpof_nIN_8gFCD40gmnfwlwlLouZQs3w \
    --OAuth2Flow AUTHORIZATION_CODE \
    --CredentialProviderId agc-******** \
    --Scopes read:user \
    --OAuth2ReturnUrl https://********************** \
    --CustomState 12********371 \
    --CustomParameters.0.Key hello \
    --CustomParameters.0.Value world \
    --ForceAuthentication False \
    --SessionUri urn:ietf:params:oauth:request_uri:****************************************************************
```

Output: 
```
{
    "Response": {
        "AuthorizationUrl": "https://auth.tencentags.com/identities/oauth2/authorize?**************************************************************************************************************",
        "SessionStatus": "IN_PROGRESS",
        "SessionUri": "urn:ietf:params:oauth:request_uri:****************************************************************",
        "RequestId": "1746590e-10dd-48a5-8fb2-794469a8e63e",
        "AccessToken": "ntn_**********************************************"
    }
}
```

