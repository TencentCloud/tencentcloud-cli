**Example 1: 后付费云联网实例修改限速类型**



Input: 

```
tccli vpc ModifyCcnRegionBandwidthLimitsType --cli-unfold-argument  \
    --CcnId ccn-gree226l \
    --BandwidthLimitType OUTER_REGION_LIMIT
```

Output: 
```
{
    "Response": {
        "RequestId": "6e446c86-d8c9-4981-9b33-d10956585058"
    }
}
```

