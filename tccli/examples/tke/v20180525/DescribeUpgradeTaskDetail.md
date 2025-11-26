**Example 1: 获取升级任务详情**

获取升级任务详情

Input: 

```
tccli tke DescribeUpgradeTaskDetail --cli-unfold-argument  \
    --ID 1 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "f1048559-c7e4-4a7b-9d12-bc0256be3e26",
        "TotalCount": 1,
        "UpgradePlans": [
            {
                "ID": 1,
                "ClusterID": "cls-12345678",
                "ClusterName": "test1",
                "PlanedStartAt": "2025-01-01 20:00:00",
                "UpgradeStartAt": "2025-01-01 20:00:00",
                "UpgradeEndAt": "2025-01-01 20:01:00",
                "Status": "Succeed"
            }
        ]
    }
}
```

