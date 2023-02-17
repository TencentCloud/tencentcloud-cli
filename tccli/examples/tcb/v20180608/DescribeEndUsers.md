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
                "UserName": "xx",
                "QQOpenId": "xx",
                "UpdateTime": "xx",
                "UUId": "xx",
                "AvatarUrl": "xx",
                "Gender": "xx",
                "IsDisabled": false,
                "IsAnonymous": true,
                "CreateTime": "xx",
                "HasPassword": true,
                "Phone": "xx",
                "WXOpenId": "xx",
                "NickName": "xx",
                "Email": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

