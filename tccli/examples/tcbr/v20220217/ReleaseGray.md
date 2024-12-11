**Example 1: 灰度发布**



Input: 

```
tccli tcbr ReleaseGray --cli-unfold-argument  \
    --EnvId abc \
    --ServerName abc \
    --GrayType abc \
    --VersionFlowItems.0.VersionName abc \
    --VersionFlowItems.0.FlowRatio 0 \
    --VersionFlowItems.0.UrlParam.Key abc \
    --VersionFlowItems.0.UrlParam.Value abc \
    --VersionFlowItems.0.Priority 0 \
    --VersionFlowItems.0.IsDefaultPriority True \
    --TrafficType abc \
    --OperatorRemark abc \
    --GrayFlowRatio 0
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

