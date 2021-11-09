**Example 1: 查询资产管理计划任务列表**



Input: 

```
tccli cwp DescribeAssetPlanTaskList --cli-unfold-argument  \
    --Uuid xx \
    --Limit 1 \
    --Quuid xx \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
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
                "OsInfo": "xx",
                "MachineName": "xx",
                "ConfigPath": "xx",
                "Command": "xx",
                "User": "xx",
                "MachineIp": "xx",
                "Cycle": "xx",
                "Quuid": "xxxx-xxxx-xxxx-xxxx",
                "Uuid": "xxxx-xxxx-xxxx-xxxx"
            }
        ],
        "RequestId": "xx",
        "Total": 1
    }
}
```

