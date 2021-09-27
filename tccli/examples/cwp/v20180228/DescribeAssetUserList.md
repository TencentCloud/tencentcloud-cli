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
                "Uuid": "xx",
                "Gid": "xx",
                "LastLoginTime": "xx",
                "MachineIp": "xx",
                "IsSshLogin": 1,
                "Status": 1,
                "Shell": "xx",
                "MachineWanIp": "xx",
                "MachineName": "xx",
                "LoginType": 1,
                "PasswordDueTime": "xx",
                "UserType": 1,
                "PasswordChangeTime": "xx",
                "HomePath": "xx",
                "OsInfo": "xx",
                "IsSudo": 1,
                "Name": "xx",
                "ProjectId": 1,
                "IsDomain": 1,
                "Uid": "xx",
                "IsRoot": 1,
                "Quuid": "xx",
                "PasswordLockDays": 1,
                "ShellLoginStatus": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

