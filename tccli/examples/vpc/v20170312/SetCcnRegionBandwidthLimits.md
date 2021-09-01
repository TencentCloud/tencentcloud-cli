**Example 1: 设置云联网各地域出带宽上限**

设置云联网各地域出带宽上限。例如在示例中，设置ap-guangzhou，ap-shanghai地域的出带宽上限分别为1000Mbps，500Mbps。

Input: 

```
tccli vpc SetCcnRegionBandwidthLimits --cli-unfold-argument  \
    --CcnId ccn-gree226l \
    --CcnRegionBandwidthLimits.0.Region ap-guangzhou \
    --CcnRegionBandwidthLimits.0.BandwidthLimit 1000 \
    --CcnRegionBandwidthLimits.1.Region ap-shanghai \
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

**Example 2: 设置云联网地域间带宽上限**

设置云联网地域间带宽上限，需要传递源和目的端地域，如果设置的是源或者目的地域为黑石地域，需要传递IsBm或者DstIsBm为true。例如在示例中，设置ap-guangzhou到ap-shanghai黑石的地域间上限为1000Mbps，设置ap-guangzhou到ap-beijing的地域间上限为500Mbps。

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

