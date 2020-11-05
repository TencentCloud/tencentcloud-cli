**Example 1: Creating a bandwidth package**



Input: 

```
tccli vpc CreateBandwidthPackage --cli-unfold-argument  \
    --ChargeType TOP5_POSTPAID_BY_MONTH\
    --NetworkType BGP
```

Output: 
```
{
    "Response": {
        "BandwidthPackageId": [
            "bwp-8rolc8ec"
        ],
        "RequestId": "57741638-47c2-4c6d-ac84-b88eb83dad06"
    }
}
```

