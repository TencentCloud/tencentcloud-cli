**Example 1: 灰度发布**



Input: 

```
tccli tcbr ReleaseGray --cli-unfold-argument  \
    --EnvId xx \
    --VersionFlowItems.0.FlowRatio 0 \
    --VersionFlowItems.0.Priority 0 \
    --VersionFlowItems.0.UrlParam.Value xx \
    --VersionFlowItems.0.UrlParam.Key xx \
    --VersionFlowItems.0.IsDefaultPriority True \
    --VersionFlowItems.0.VersionName xx \
    --ServerName xx \
    --TrafficType xx \
    --GrayType xx \
    --GrayFlowRatio 0 \
    --OperatorRemark xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

