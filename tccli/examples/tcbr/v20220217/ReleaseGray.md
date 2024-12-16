**Example 1: 灰度发布**



Input: 

```
tccli tcbr ReleaseGray --cli-unfold-argument  \
    --EnvId env-sdfsdf \
    --ServerName server-sdfsdf \
    --GrayType FLOW \
    --VersionFlowItems.0.VersionName version-sdfsdf \
    --VersionFlowItems.0.FlowRatio 50 \
    --VersionFlowItems.0.UrlParam.Key key \
    --VersionFlowItems.0.UrlParam.Value value \
    --VersionFlowItems.0.Priority 0 \
    --VersionFlowItems.0.IsDefaultPriority True \
    --TrafficType  \
    --OperatorRemark remark \
    --GrayFlowRatio 0
```

Output: 
```
{
    "Response": {
        "RequestId": "sdfsdfsdf"
    }
}
```

