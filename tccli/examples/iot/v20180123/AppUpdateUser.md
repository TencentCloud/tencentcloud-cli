**Example 1: 更新用户信息**

更新用户信息

Input: 

```
tccli iot AppUpdateUser --cli-unfold-argument  \
    --NickName abc \
    --AccessToken xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "abcfb085-4db0-4da7-a7c1-55d5f5bfc6e7",
        "AppUser": {
            "ApplicationId": "app-hwgab41y",
            "UserName": "username",
            "CreateTime": "2018-05-01 20:38:20",
            "NickName": "昵称",
            "UpdateTime": "2018-05-01 20:58:48"
        }
    }
}
```

