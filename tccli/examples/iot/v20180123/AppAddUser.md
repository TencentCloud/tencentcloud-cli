**Example 1: 注册应用用户**

注册应用用户

Input: 

```
tccli iot AppAddUser --cli-unfold-argument  \
    --UserName iotappuser \
    --Password iotappuser666!
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

