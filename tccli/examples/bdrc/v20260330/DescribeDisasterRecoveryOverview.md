**Example 1: 查询当前容灾概览**



Input: 

```
tccli bdrc DescribeDisasterRecoveryOverview --cli-unfold-argument  \
    --CopyPairType ALL
```

Output: 
```
{
    "Response": {
        "DisasterRecoveryOverview": {
            "CopyPairCount": 5,
            "CopyPairErrorRPOCount": 2,
            "CopyPairSuccessRPOCount": 3,
            "DrillPairCount": 2,
            "DrillPairDrillingCount": 0,
            "DrillPairFailedCount": 0,
            "DrillPairSuccessCount": 2,
            "FailoverFailedCount": 0,
            "ProtectGroupCount": 296,
            "ProtectGroupCrossCloudCount": 0,
            "ProtectGroupCrossRegionCount": 0,
            "ProtectGroupCrossZoneCount": 296,
            "ProtectedResourceCopyingCount": 2,
            "ProtectedResourceCount": 5,
            "ProtectedResourceStoppedCount": 3,
            "SitePairCount": 2,
            "SitePairCrossCloudCount": 0,
            "SitePairCrossRegionCount": 0,
            "SitePairCrossZoneCount": 2
        },
        "OverviewInRegionSet": [
            {
                "CopyPairCount": 5,
                "CopyPairErrorRPOCount": 2,
                "CopyPairSuccessRPOCount": 3,
                "DrillPairCount": 2,
                "DrillPairDrillingCount": 0,
                "DrillPairFailedCount": 0,
                "DrillPairSuccessCount": 2,
                "FailoverFailedCount": 0,
                "ProtectGroupCount": 296,
                "ProtectGroupCrossCloudCount": 0,
                "ProtectGroupCrossRegionCount": 0,
                "ProtectGroupCrossZoneCount": 296,
                "ProtectedResourceCopyingCount": 2,
                "ProtectedResourceCount": 5,
                "ProtectedResourceStoppedCount": 3,
                "Region": "ap-guangzhou",
                "SitePairCount": 2,
                "SitePairCrossCloudCount": 0,
                "SitePairCrossRegionCount": 0,
                "SitePairCrossZoneCount": 2
            }
        ],
        "RequestId": "9fd291d3-19d9-4214-b53f-10f438959210"
    }
}
```

