**Example 1: 查询资产管理计划任务列表**



Input: 

```
tccli cwp DescribeAssetPlanTaskList --cli-unfold-argument  \
    --Uuid 65ce6db8-a914-4349-a8b9-d756236686d2 \
    --Limit 1 \
    --Quuid 65ce6db8-a914-4349-a8b9-d756236686d2 \
    --Filters.0.Values 10.0.0.1 \
    --Filters.0.Name IP \
    --Filters.0.ExactMatch True \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Tasks": [
            {
                "Status": 1,
                "Cycle": "10 * * * *",
                "Command": "/root/test",
                "User": "root",
                "ConfigPath": "/root",
                "MachineIp": "10.0.0.11",
                "MachineName": "test-name",
                "OsInfo": "CentOs Bit64",
                "Quuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "Uuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "UpdateTime": "2024-10-11 12:23:34",
                "FirstTime": "2024-10-11 12:23:34",
                "IsNew": 0,
                "MachineWanIp": "110.84.0.11",
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
        "Total": 1,
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

