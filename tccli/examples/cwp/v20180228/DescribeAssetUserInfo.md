**Example 1: 获取主机账号详情**



Input: 

```
tccli cwp DescribeAssetUserInfo --cli-unfold-argument  \
    --Quuid 24c9be55-c743-4a75-a5c7-2a2912341234 \
    --Uuid 24c9be55-c743-4a75-a5c7-2a2912341234 \
    --Name test_user
```

Output: 
```
{
    "Response": {
        "User": {
            "MachineIp": "10.0.0.11",
            "MachineName": "test-name",
            "Uuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
            "Quuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
            "Uid": "1011223",
            "Gid": "1011223",
            "Status": 1,
            "IsRoot": 1,
            "LastLoginTime": "2024-10-11 12:23:34",
            "Name": "test-name",
            "UserType": 1,
            "IsDomain": 1,
            "IsSshLogin": 1,
            "HomePath": "/root",
            "Shell": "/bin/sh",
            "ShellLoginStatus": 1,
            "PasswordChangeTime": "2024-10-11 12:23:34",
            "PasswordDueTime": "2024-10-11 12:23:34",
            "PasswordLockDays": 0,
            "Remark": "",
            "GroupName": "test-name",
            "DisableTime": "2024-10-11 12:23:34",
            "LastLoginTerminal": "test",
            "LastLoginLoc": "usa",
            "LastLoginIp": "10.0.0.11",
            "PasswordWarnDays": 1,
            "PasswordChangeType": 1,
            "Keys": [
                {
                    "Value": "test1",
                    "Comment": "name",
                    "EncryptType": "md5"
                }
            ],
            "UpdateTime": "2024-10-11 12:23:34"
        },
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

