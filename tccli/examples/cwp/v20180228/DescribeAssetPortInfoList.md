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
                "MachineIp": "10.0.0.11",
                "MachineWanIp": "110.84.0.11",
                "Quuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "Uuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "OsInfo": "CentOs Bit64",
                "ProjectId": 1,
                "Tag": [
                    {
                        "Rid": 0,
                        "Name": "test-name",
                        "TagId": 1
                    }
                ],
                "ProcessName": "test-name",
                "ProcessVersion": "0.1.1",
                "ProcessPath": "/data",
                "Pid": "1024",
                "User": "root",
                "StartTime": "2024-10-11 12:23:34",
                "Param": "null",
                "Teletype": "1",
                "Port": "22",
                "GroupName": "test-name",
                "Md5": "708cae4cf814c3deda4208da228fad4e",
                "Ppid": "1",
                "ParentProcessName": "test-name",
                "Proto": "http",
                "BindIp": "10.0.0.11",
                "MachineName": "test-name",
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

