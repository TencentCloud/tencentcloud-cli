**Example 1: 查询定时任务列表**

基线设置 查询定时任务列表

Input: 

```
tccli tcss DescribeCompliancePeriodTaskList --cli-unfold-argument  \
    --AssetType ASSET_CONTAINER \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx",
        "TotalCount": 1,
        "PeriodTaskSet": [
            {
                "PeriodTaskId": 123,
                "AssetType": "xxxx",
                "PeriodRule": {
                    "ExecutionTime": "xx",
                    "Frequency": 1
                },
                "LastTriggerTime": "YYYY-MM-DD HH:mm:SS",
                "TotalPolicyItemCount": 123,
                "BenchmarkStandardSet": [
                    {
                        "StandardId": 12345,
                        "Name": "CIS Docker",
                        "Description": "CIS Docker",
                        "PolicyItemCount": 123,
                        "Enabled": true
                    }
                ]
            }
        ]
    }
}
```

