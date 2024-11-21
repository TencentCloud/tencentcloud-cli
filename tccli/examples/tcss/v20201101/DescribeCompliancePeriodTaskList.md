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
        "RequestId": "3e6756ce-6512-498d-a9fd-8572ef4ce7d3",
        "TotalCount": 1,
        "PeriodTaskSet": [
            {
                "PeriodTaskId": 456,
                "AssetType": "ASSET_CONTAINER",
                "PeriodRule": {
                    "ExecutionTime": "2006-01-02 15:04:05",
                    "Frequency": 1
                },
                "LastTriggerTime": "2006-01-02 15:04:05",
                "TotalPolicyItemCount": 345634,
                "BenchmarkStandardSet": [
                    {
                        "StandardId": 2342,
                        "Name": "CIS Docker",
                        "Description": "CIS Docker",
                        "PolicyItemCount": 666,
                        "Enabled": true
                    }
                ]
            }
        ]
    }
}
```

