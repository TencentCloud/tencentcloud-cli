**Example 1: 获取资产管理端口列表**



Input: 

```
tccli cwp DescribeAssetPortInfoList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Ports": [
            {
                "Uuid": "xx",
                "Proto": "xx",
                "Param": "xx",
                "ProcessVersion": "xx",
                "MachineIp": "xx",
                "Teletype": "xx",
                "Ppid": "xx",
                "MachineWanIp": "xx",
                "MachineName": "xx",
                "User": "xx",
                "BindIp": "xx",
                "Md5": "xx",
                "OsInfo": "xx",
                "ProjectId": 1,
                "GroupName": "xx",
                "ProcessPath": "xx",
                "ProcessName": "xx",
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
                "Port": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

