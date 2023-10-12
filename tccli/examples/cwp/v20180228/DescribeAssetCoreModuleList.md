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
                "Name": "abc",
                "Desc": "abc",
                "Path": "abc",
                "Version": "abc",
                "MachineIp": "abc",
                "MachineName": "abc",
                "OsInfo": "abc",
                "Size": 1,
                "ProcessCount": 1,
                "ModuleCount": 1,
                "Id": "abc",
                "Quuid": "abc",
                "Uuid": "abc",
                "UpdateTime": "abc",
                "FirstTime": "abc",
                "IsNew": 0,
                "MachineWanIp": "abc",
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
        "Total": 1,
        "RequestId": "abc"
    }
}
```

