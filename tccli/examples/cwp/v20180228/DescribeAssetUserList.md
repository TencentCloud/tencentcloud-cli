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
                "MachineIp": "10.0.0.11",
                "MachineWanIp": "110.84.0.11",
                "MachineName": "test-name",
                "OsInfo": "CentOs Bit64",
                "Uuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "Quuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "Uid": "abc",
                "Gid": "abc",
                "Status": 1,
                "IsRoot": 1,
                "LoginType": 1,
                "LastLoginTime": "2024-10-11 12:23:34",
                "Name": "test-name",
                "ProjectId": 1,
                "UserType": 1,
                "IsDomain": 1,
                "IsSudo": 1,
                "IsSshLogin": 1,
                "HomePath": "/root",
                "Shell": "/bin/sh",
                "ShellLoginStatus": 1,
                "PasswordChangeTime": "2024-10-11 12:23:34",
                "PasswordDueTime": "2024-10-11 12:23:34",
                "PasswordLockDays": 0,
                "PasswordStatus": 0,
                "UpdateTime": "2024-10-11 12:23:34",
                "FirstTime": "2024-10-11 12:23:34",
                "IsNew": 0,
                "MachineExtraInfo": {
                    "WanIP": "110.84.0.11",
                    "PrivateIP": "10.0.0.11",
                    "NetworkType": 0,
                    "NetworkName": "vpc-12341234",
                    "InstanceID": "ins-aj28fjz",
                    "HostName": "test-name"
                }
            }
        ],
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

