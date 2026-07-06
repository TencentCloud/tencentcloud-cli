**Example 1: 创建增强型月95带宽包**



Input: 

```
tccli vpc CreateBandwidthPackage --cli-unfold-argument  \
    --NetworkType BGP \
    --ChargeType ENHANCED95_POSTPAID_BY_MONTH \
    --BandwidthPackageName test_name \
    --BandwidthPackageCount 1 \
    --InternetMaxBandwidth 300
```

Output: 
```
{
    "Response": {
        "BandwidthPackageId": "bwp-63pghhwp",
        "BandwidthPackageIds": [
            "bwp-63pghhwp"
        ],
        "RequestId": "9e8b2fc1-ef7c-4f07-b461-e884e45a4270"
    }
}
```

