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
                "Cycle": "abc",
                "Command": "abc",
                "User": "abc",
                "ConfigPath": "abc",
                "MachineIp": "abc",
                "MachineName": "abc",
                "OsInfo": "abc",
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

