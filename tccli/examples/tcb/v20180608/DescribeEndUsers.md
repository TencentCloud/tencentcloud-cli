**Example 1: 获取终端用户列表**



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
        "RequestId": "dee235ec-b92e-4ca7-a3e7-77d2410ab776",
        "Total": 1,
        "Users": [
            {
                "UUId": "00000000963b4a85a9b34e2d1fe0c685",
                "WXOpenId": "",
                "QQOpenId": "",
                "Phone": "",
                "Email": "",
                "NickName": "",
                "Gender": "",
                "AvatarUrl": "",
                "UpdateTime": "",
                "CreateTime": "2020-03-04 18:08:13",
                "IsAnonymous": true,
                "IsDisabled": false
            }
        ]
    }
}
```

