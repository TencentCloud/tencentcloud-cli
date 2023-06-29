**Example 1: 获取用户第三方开放平台的access token**



Input: 

```
tccli open GetUserAccessToken --cli-unfold-argument  \
    --UserAuthCode aaa \
    --OpenAccessToken bbb
```

Output: 
```
{
    "Response": {
        "AppId": "100005604499",
        "UserOpenId": "391f920b807ecbaa38f7e77ef5260cd4",
        "UserUnionId": "438344612f5e181dbb76d2fcf2634a7b",
        "UserAccessToken": "a649830709416d07be8f0dba1c7675ce",
        "ExpiresAt": 1581670707,
        "UserRefreshToken": "607202ece53c20a8ad91fa3512fa8ac7",
        "Scope": "login",
        "RequestId": "5bc7a27e-ba54-4b68-b37e-aaee60a2c5e2"
    }
}
```

