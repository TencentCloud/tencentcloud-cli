**Example 1: 校验IdP登录响应**



Input: 

```
tccli cloudapp VerifyIdPConnectionResponse --cli-unfold-argument  \
    --CloudappId cloudapp-1m42xxxx \
    --SAMLResponseBase64 W5hdGlvbj0iaHR0cHM6Ly9zaG...
```

Output: 
```
{
    "Response": {
        "RequestId": "5a83a1cb-598a-e607-a72c-8d4530b24796",
        "UserInfo": {
            "UserId": "100001201",
            "UserName": "张三",
            "Email": "zhang3@your.idp",
            "Phone": "133000001",
            "UserRole": "role:readwrite:xxx",
            "Avatar": "https://your.idp/user/zhang3/avatar.png"
        }
    }
}
```

