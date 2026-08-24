**Example 1: 查询站点对列表**



Input: 

```
tccli bdrc DescribeDisasterRecoverySitePairs --cli-unfold-argument  \
    --SitePairType INSTANCE \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "SitePairSet": [
            {
                "AccountUin": "700002591018",
                "AppId": 260147302,
                "BindProtectGroupCount": 4,
                "CopyType": "ASY",
                "CreateFrom": "LOCAL",
                "CreateTime": "2026-06-01 16:14:29",
                "CrossCloudDetails": null,
                "DisasterRecoveryType": "CROSS_ZONE",
                "ErrorRecoveryPointObjectiveCopyPairSet": [],
                "ProtectedResourceSet": [
                    {
                        "ResourceIdSet": [
                            "ins-8tjecaei"
                        ],
                        "ResourceType": "INSTANCE"
                    }
                ],
                "ProtectedResourceStatusSet": [
                    {
                        "Count": 6,
                        "Status": "FULL_COPYING"
                    }
                ],
                "SitePairId": "sitepair-po028nwp",
                "SitePairName": "drc_az",
                "SitePairState": "NORMAL",
                "SitePairType": "INSTANCE",
                "SourceRegion": "ap-guangzhou",
                "SourceVpc": "vpc-mfgxt19j",
                "SourceZone": "ap-guangzhou-2",
                "SubAccountUin": "700002591018",
                "TargetRegion": "ap-guangzhou",
                "TargetVpc": "vpc-mfgxt19j",
                "TargetZone": "ap-guangzhou-3"
            }
        ],
        "TotalCount": 41,
        "RequestId": "08f41fce-913a-47c4-96fa-c5d38158e759"
    }
}
```

