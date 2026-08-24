**Example 1: 查询保护组**



Input: 

```
tccli bdrc DescribeDisasterRecoveryProtectGroups --cli-unfold-argument  \
    --ProtectGroupType INSTANCE \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "ProtectGroupSet": [
            {
                "AccountUin": "700002579593",
                "AppId": 260132668,
                "BindProtectedResourceCount": 1,
                "CopyType": "ASY",
                "CreateFrom": "LOCAL",
                "CreateTime": "2026-06-09 11:25:39",
                "DataDirection": "POSITIVE",
                "DisasterRecoveryType": "CROSS_ZONE",
                "ErrorRecoveryPointObjectiveCount": 0,
                "LifeState": "NORMAL",
                "ModifyTime": "2026-06-09 11:25:39",
                "ProtectGroupId": "pg-awh08zgp",
                "ProtectGroupName": "pg5-new",
                "ProtectGroupType": "INSTANCE",
                "ProtectedResourceStatusSet": [
                    {
                        "Count": 1,
                        "Status": "INIT"
                    }
                ],
                "RecoveryPointObjective": 15,
                "SitePairId": "sitepair-0wxbktxr",
                "SitePairName": "scenario-lifecycle-test-sitepair",
                "SourceRegion": "ap-guangzhou",
                "SourceVpc": "vpc-i9pwklpn",
                "SourceZone": "ap-guangzhou-2",
                "SubAccountUin": "700002579593",
                "TargetRegion": "ap-guangzhou",
                "TargetVpc": "vpc-ap4fkwyt",
                "TargetZone": "ap-guangzhou-3"
            }
        ],
        "TotalCount": 294,
        "RequestId": "3e397705-f35f-4cdd-83f5-e02ba22aa567"
    }
}
```

