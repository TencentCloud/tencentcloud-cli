**Example 1: 创建容灾策略**



Input: 

```
tccli bdrc CreateDisasterRecoverySitePair --cli-unfold-argument  \
    --DisasterRecoveryType CROSS_ZONE \
    --SourceRegion ap-guangzhou \
    --SourceZone ap-guangzhou-2 \
    --TargetRegion ap-guangzhou \
    --TargetZone ap-guangzhou-3 \
    --SourceVpc vpc-i9pwklpn \
    --TargetVpc vpc-ap4fkwyt \
    --SitePairProductType INSTANCE \
    --SitePairName fromapi-1 \
    --CopyType ASY
```

Output: 
```
{
    "Response": {
        "SitePairId": "sitepair-3k23fkmn",
        "RequestId": "8e63c7c6-d644-4520-b3fa-c26e4aa13b67"
    }
}
```

