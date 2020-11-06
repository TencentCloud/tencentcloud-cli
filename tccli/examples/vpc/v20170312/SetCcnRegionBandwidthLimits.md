**Example 1: Setting the outbound bandwidth limit for CCN regions**

This example shows you how to set the outbound bandwidth limit for CCN regions. In this case, we will set the limit for `ap-guangzhou` to 1,000 Mbps and `ap-shanghai` to 500 Mbps.

Input: 

```
tccli vpc SetCcnRegionBandwidthLimits --cli-unfold-argument  \
    --CcnId ccn-gree226l \
    --CcnRegionBandwidthLimits.0.Region ap-guangzhou \
    --CcnRegionBandwidthLimits.0.BandwidthLimit 1000 \
    --CcnRegionBandwidthLimits.1.Region ap-guangzhou \
    --CcnRegionBandwidthLimits.1.BandwidthLimit 500
```

Output: 
```
{
    "Response": {
        "RequestId": "9c53ff69-1bb6-4c89-adbb-812233a85acc"
    }
}
```

**Example 2: Setting the inter-region bandwidth limit for CCN regions**

This example shows you how to set the inter-region bandwidth limit by specifying the source and destination regions. If the source or destination region is a BM reregion, you need to set the `IsBm` or `DstIsBm` parameter to be `true`. In the example, the inter-region bandwidth limit between ap-guangzhou and ap-shanghai BM regions is 1,000 Mbps, and that between ap-guangzhou and ap-beijing region is 500 Mbps.

Input: 

```
tccli vpc SetCcnRegionBandwidthLimits --cli-unfold-argument  \
    --CcnId ccn-gree226l \
    --CcnRegionBandwidthLimits.0.Region ap-guangzhou \
    --CcnRegionBandwidthLimits.0.BandwidthLimit 1000 \
    --CcnRegionBandwidthLimits.0.DstRegion ap-shanghai \
    --CcnRegionBandwidthLimits.0.DstIsBm true \
    --CcnRegionBandwidthLimits.1.Region ap-guangzhou \
    --CcnRegionBandwidthLimits.1.BandwidthLimit 500 \
    --CcnRegionBandwidthLimits.1.DstRegion ap-beijing
```

Output: 
```
{
    "Response": {
        "RequestId": "9c53ff69-1bb6-4c89-adbb-812233a85acc"
    }
}
```

