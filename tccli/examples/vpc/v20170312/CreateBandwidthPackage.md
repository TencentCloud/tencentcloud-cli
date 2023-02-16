**Example 1: 创建共享带宽包**

创建共享带宽包

Input: 

```
tccli vpc CreateBandwidthPackage --cli-unfold-argument  \
    --NetworkType BGP \
    --ChargeType TOP5_POSTPAID_BY_MONTH
```

Output: 
```
{
    "Response": {
        "BandwidthPackageId": "bwp-8rol****",
        "BandwidthPackageIds": [
            "bwp-8rol****"
        ],
        "RequestId": "57741638-47c2-4c6d-ac84-b88eb83dad06"
    }
}
```

