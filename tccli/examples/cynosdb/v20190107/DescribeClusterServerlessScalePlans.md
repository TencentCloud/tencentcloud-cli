**Example 1: 查询计划**



Input: 

```
tccli cynosdb DescribeClusterServerlessScalePlans --cli-unfold-argument  \
    --ClusterId cynosdbmysql-xdbsbsgg \
    --PlanId 12541
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ServerlessScalePlans": [
            {
                "PlanId": 1231,
                "ClusterId": "cynosdbmysql-xbhshsbh",
                "ObjectInstance": "cynosdbmysql-ins-xbhshsbh",
                "PolicyId": "cynosdbmysql-spd-rye0gd5b",
                "PolicyType": "PolicyTypePeriodScale",
                "SourceMinCpu": "1.0",
                "SourceMaxCpu": "8.0",
                "TargetMinCpu": "2.0",
                "TargetMaxCpu": "4.0",
                "ExpectedStartTime": "2025-12-01 00:12:00",
                "ExpectedEndTime": "2025-12-01 00:20:00",
                "Status": "success",
                "ScaleTaskId": 131,
                "FailReason": "",
                "ResetTaskId": 0
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

