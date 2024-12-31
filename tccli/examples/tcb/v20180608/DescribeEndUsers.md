**Example 1: 获取终端用户列表**

获取终端用户列表

Input: 

```
tccli tcb DescribeEndUsers --cli-unfold-argument  \
    --EnvId envid \
    --UUIds 00000000963b4a85a9b34e2d1fe0c685
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Users": [
            {
                "UserName": "admin",
                "QQOpenId": "openid123",
                "UpdateTime": "2025-01-01",
                "UUId": "abc123",
                "AvatarUrl": "https://www.baidu.com",
                "Gender": "male",
                "IsDisabled": false,
                "IsAnonymous": true,
                "CreateTime": "2025-01-01",
                "HasPassword": true,
                "Phone": "13092030921",
                "WXOpenId": "openwx123",
                "NickName": "steven",
                "Email": "steven@tencent.com"
            }
        ],
        "RequestId": "abc12345667"
    }
}
```

