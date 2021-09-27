**Example 1: 获取主机账号详情**



Input: 

```
tccli cwp DescribeAssetUserInfo --cli-unfold-argument  \
    --Quuid xx \
    --Uuid xx \
    --Name xx
```

Output: 
```
{
    "Response": {
        "User": {
            "Uuid": "xx",
            "LastLoginIp": "xx",
            "Gid": "xx",
            "PasswordChangeType": 1,
            "LastLoginTime": "xx",
            "MachineIp": "xx",
            "IsSshLogin": 1,
            "Status": 1,
            "UpdateTime": "xx",
            "Shell": "xx",
            "IsDomain": 1,
            "Keys": [
                {
                    "Comment": "xx",
                    "EncryptType": "xx",
                    "Value": "xx"
                }
            ],
            "MachineName": "xx",
            "PasswordDueTime": "xx",
            "UserType": 1,
            "PasswordChangeTime": "xx",
            "HomePath": "xx",
            "Remark": "xx",
            "Name": "xx",
            "GroupName": "xx",
            "DisableTime": "xx",
            "LastLoginLoc": "xx",
            "Uid": "xx",
            "IsRoot": 1,
            "LastLoginTerminal": "xx",
            "Quuid": "xx",
            "PasswordLockDays": 0,
            "ShellLoginStatus": 1,
            "PasswordWarnDays": 1
        },
        "RequestId": "xx"
    }
}
```

