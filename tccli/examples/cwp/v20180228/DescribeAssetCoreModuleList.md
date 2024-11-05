**Example 1: 查询资产管理内核模块列表**



Input: 

```
tccli cwp DescribeAssetCoreModuleList --cli-unfold-argument  \
    --Uuid 65ce6db8-a914-4349-a8b9-d756236686d2 \
    --Order asc \
    --Limit 1 \
    --Quuid 65ce6db8-a914-4349-a8b9-d756236686d2 \
    --Offset 1 \
    --By Size
```

Output: 
```
{
    "Response": {
        "Modules": [
            {
                "Name": "test-name",
                "Desc": "idesc",
                "Path": "/root",
                "Version": "0.1.1",
                "MachineIp": "1.1.1.1",
                "MachineName": "test-name",
                "OsInfo": "CentOs Bit64",
                "Size": 1,
                "ProcessCount": 1,
                "ModuleCount": 1,
                "Id": "1024",
                "Quuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "Uuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "UpdateTime": "2024-10-11 12:23:34",
                "FirstTime": "2024-10-11 12:23:34",
                "IsNew": 0,
                "MachineWanIp": "1.1.1.1",
                "MachineExtraInfo": {
                    "WanIP": "1.1.1.1",
                    "PrivateIP": "1.1.1.1",
                    "NetworkType": 0,
                    "NetworkName": "vpc-id",
                    "InstanceID": "ins-id",
                    "HostName": "test-name"
                }
            }
        ],
        "Total": 1,
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

