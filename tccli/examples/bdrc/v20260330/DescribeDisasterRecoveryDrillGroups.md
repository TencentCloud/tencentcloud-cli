**Example 1: 查询演练组列表**



Input: 

```
tccli bdrc DescribeDisasterRecoveryDrillGroups --cli-unfold-argument  \
    --DrillGroupType INSTANCE
```

Output: 
```
{
    "Response": {
        "DrillGroupSet": [
            {
                "AccountUin": "700002579593",
                "AppId": 260132668,
                "BindDrilledResourceCount": 1,
                "CopyType": "ASY",
                "CreateTime": "2026-06-08 21:17:16",
                "DataDirection": "POSITIVE",
                "DisasterRecoveryType": "CROSS_ZONE",
                "DrillGroupId": "dg-flxbvmo3",
                "DrillGroupName": "drll tee new",
                "DrillGroupType": "INSTANCE",
                "DrillRegion": "ap-guangzhou",
                "DrillSecurityGroup": null,
                "DrillVpc": "vpc-3pwbhict",
                "DrillZone": "ap-guangzhou-3",
                "DrilledResourceStatusSet": [
                    {
                        "ResourceCount": 1,
                        "ResourceStatus": "NORMAL"
                    }
                ],
                "Id": 48,
                "LifeState": "NORMAL",
                "LocalCloudName": null,
                "ModifyTime": "2026-06-09 10:50:10",
                "PeerCloudName": null,
                "ProtectGroupId": "pg-4tqdwtqj",
                "RecoveryTime": null,
                "SitePairId": "sitepair-0wxbktxr",
                "SourceRegion": "ap-guangzhou",
                "SourceVpc": "vpc-i9pwklpn",
                "SourceZone": "ap-guangzhou-2",
                "SubAccountUin": "700002579593"
            }
        ],
        "TotalCount": 2,
        "RequestId": "77ab184f-e266-4fb7-b152-b3152eda3074"
    }
}
```

