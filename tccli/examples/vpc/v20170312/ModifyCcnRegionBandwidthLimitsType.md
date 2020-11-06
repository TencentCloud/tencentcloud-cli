**Example 1: Changes the bandwidth limit type of a postpaid CCN instance**



Input: 

```
tccli vpc ModifyCcnRegionBandwidthLimitsType --cli-unfold-argument  \
    --Version 2017-03-12 \
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

