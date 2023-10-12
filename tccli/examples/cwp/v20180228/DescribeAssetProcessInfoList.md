**Example 1: 获取资产管理进程列表**



Input: 

```
tccli cwp DescribeAssetProcessInfoList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Process": [
            {
                "MachineIp": "abc",
                "MachineWanIp": "abc",
                "Quuid": "abc",
                "Uuid": "abc",
                "OsInfo": "abc",
                "ProjectId": 1,
                "Tag": [
                    {
                        "Rid": 0,
                        "Name": "abc",
                        "TagId": 1
                    }
                ],
                "Name": "abc",
                "Desc": "abc",
                "Path": "abc",
                "Pid": "abc",
                "User": "abc",
                "StartTime": "abc",
                "Param": "abc",
                "Tty": "abc",
                "Version": "abc",
                "GroupName": "abc",
                "Md5": "abc",
                "Ppid": "abc",
                "ParentProcessName": "abc",
                "Status": "abc",
                "HasSign": 1,
                "InstallByPackage": 1,
                "PackageName": "abc",
                "MachineName": "abc",
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

