**Example 1: 获取资产管理进程列表**



Input: 

```
tccli cwp DescribeAssetProcessInfoList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Process": [
            {
                "HasSign": 1,
                "Uuid": "xx",
                "PackageName": "xx",
                "Param": "xx",
                "Version": "xx",
                "Ppid": "xx",
                "MachineIp": "xx",
                "Status": "xx",
                "MachineWanIp": "xx",
                "MachineName": "xx",
                "User": "xx",
                "Path": "xx",
                "Md5": "xx",
                "OsInfo": "xx",
                "Name": "xx",
                "ProjectId": 1,
                "GroupName": "xx",
                "Tty": "xx",
                "InstallByPackage": 1,
                "ParentProcessName": "xx",
                "Pid": "xx",
                "Tag": [
                    {
                        "TagId": 1,
                        "Rid": 0,
                        "Name": "xx"
                    }
                ],
                "Quuid": "xx",
                "StartTime": "xx",
                "Desc": "xx"
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

