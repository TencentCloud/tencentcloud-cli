**Example 1: 获取计划升级任务**

获取计划升级任务

Input: 

```
tccli tke DescribeUpgradeTasks --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "f1048559-c7e4-4a7b-9d12-bc0256be3e26",
        "TotalCount": 1,
        "UpgradeTasks": [
            {
                "ID": 1,
                "Name": "coredns基线化升级",
                "Component": "coredns",
                "RelatedResources": [
                    "coredns"
                ],
                "UpgradeImpact": "集群域名解析延迟有抖动",
                "PlanedStartAt": "2025-01-05 20:00:00",
                "CreatedAt": "2025-01-02 20:00:00"
            }
        ]
    }
}
```

