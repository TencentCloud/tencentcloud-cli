**Example 1: 获取用户信息**

获取用户信息

Input: 

```
tccli iot AppGetUser --cli-unfold-argument  \
    --AccessToken xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "a83c028f-5a7a-43b0-b9c5-65ec72837535",
        "AppUser": {
            "ApplicationId": "app-hwgab41y",
            "UserName": "username",
            "CreateTime": "2018-05-01 20:38:20",
            "NickName": "",
            "UpdateTime": "2018-05-01 20:38:20"
        }
    }
}
```

