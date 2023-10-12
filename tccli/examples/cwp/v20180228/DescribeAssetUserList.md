**Example 1: 获取账号列表**



Input: 

```
tccli cwp DescribeAssetUserList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Users": [
            {
                "MachineIp": "abc",
                "MachineWanIp": "abc",
                "MachineName": "abc",
                "OsInfo": "abc",
                "Uuid": "abc",
                "Quuid": "abc",
                "Uid": "abc",
                "Gid": "abc",
                "Status": 1,
                "IsRoot": 1,
                "LoginType": 1,
                "LastLoginTime": "abc",
                "Name": "abc",
                "ProjectId": 1,
                "UserType": 1,
                "IsDomain": 1,
                "IsSudo": 1,
                "IsSshLogin": 1,
                "HomePath": "abc",
                "Shell": "abc",
                "ShellLoginStatus": 1,
                "PasswordChangeTime": "abc",
                "PasswordDueTime": "abc",
                "PasswordLockDays": 0,
                "PasswordStatus": 0,
                "UpdateTime": "abc",
                "FirstTime": "abc",
                "IsNew": 0,
                "MachineExtraInfo": {
                    "WanIP": "abc",
                    "PrivateIP": "abc",
                    "NetworkType": 0,
                    "NetworkName": "abc",
                    "InstanceID": "abc",
                    "HostName": "abc"
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

