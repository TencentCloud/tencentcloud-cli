**Example 1: 查询复制对**



Input: 

```
tccli bdrc DescribeCopyPairs --cli-unfold-argument  \
    --Limit 1 \
    --CopyPairType INSTANCE
```

Output: 
```
{
    "Response": {
        "CopyPairSet": [
            {
                "AccountUin": "700002579593",
                "AppId": 260132668,
                "CopyPairId": "cvmcopypair-ibd2jvbj",
                "CopyPairName": "t5-0",
                "CopyPairState": "INIT",
                "CopyPairType": "INSTANCE",
                "CreateFrom": "LOCAL",
                "CreateTime": "2026-06-09 12:00:16",
                "DataDirection": "POSITIVE",
                "DeferredCreate": true,
                "DisasterRecoveryType": "CROSS_ZONE",
                "DiskCopyPairSet": [
                    {
                        "CopyPairId": "copypair-9wgl3suj",
                        "CopyPairName": "t5-0-0",
                        "CreateTime": "2026-06-09 12:00:16",
                        "SourceResourceId": "disk-a8ys45xk",
                        "TargetResourceId": ""
                    }
                ],
                "DrillGroupId": null,
                "InstanceCopyPairId": "cvmcopypair-ibd2jvbj",
                "InstanceId": "ins-ggpv137w",
                "LatestProtectionTime": null,
                "PeerCloudName": null,
                "Percent": null,
                "ProtectGroupId": "pg-awh08zgp",
                "ProtectGroupName": "pg5-new",
                "ProtectionTimeSet": null,
                "RecoveryPointObjective": 15,
                "RollbackPercent": 0,
                "Rollbacking": 0,
                "SitePairId": "sitepair-0wxbktxr",
                "SitePairName": "scenario-lifecycle-test-sitepair",
                "SourceRegion": "ap-guangzhou",
                "SourceResourceId": "ins-ggpv137w",
                "SourceVpc": "vpc-i9pwklpn",
                "SourceZone": "ap-guangzhou-2",
                "SubAccountUin": "700002579593",
                "TargetCvmCreated": false,
                "TargetRegion": "ap-guangzhou",
                "TargetResourceId": "drp-17ixt9oj",
                "TargetVpc": "vpc-ap4fkwyt",
                "TargetZone": "ap-guangzhou-3"
            }
        ],
        "TotalCount": 5,
        "RequestId": "58fa46d6-954d-45dd-a2ee-4422e77d5c34"
    }
}
```

