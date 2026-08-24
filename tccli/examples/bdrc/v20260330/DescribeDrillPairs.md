**Example 1: 查询演练对**



Input: 

```
tccli bdrc DescribeDrillPairs --cli-unfold-argument  \
    --DrillPairType INSTANCE
```

Output: 
```
{
    "Response": {
        "DrillPairSet": [
            {
                "AccountUin": "700002579593",
                "AppId": 260132668,
                "CopyPairId": "cvmcopypair-ifytsjpr",
                "CopyPairName": "t3-0-new",
                "CreateTime": "2026-06-08 21:17:17",
                "DrillGroupId": "dg-flxbvmo3",
                "DrillGroupName": "drll tee new",
                "DrillPairId": "drillpair-p50csne5",
                "DrillPairName": "NewGroup",
                "DrillPairState": "NORMAL",
                "DrillPairType": "INSTANCE",
                "EndTime": "2026-06-08 21:19:05",
                "ProtectGroupId": "pg-4tqdwtqj",
                "RecoveryTime": "2026-06-05 17:50:09",
                "RollbackPercent": 0,
                "Rollbacking": 0,
                "SitePairId": "sitepair-0wxbktxr",
                "Size": 60,
                "SourceRegion": "ap-guangzhou",
                "SourceResourceId": "ins-q8gh28qy",
                "SourceZone": "ap-guangzhou-2",
                "SubAccountUin": "700002579593",
                "TargetRegion": "ap-guangzhou",
                "TargetResourceId": "ins-3bpdkqti",
                "TargetZone": "ap-guangzhou-3"
            }
        ],
        "TotalCount": 2,
        "RequestId": "2d67a4d7-649b-4620-a831-366475d71cac"
    }
}
```

