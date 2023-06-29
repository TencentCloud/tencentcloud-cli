**Example 1: 修改机房设备信息**

修改机房设备信息

Input: 

```
tccli cdc ModifySiteDeviceInfo --cli-unfold-argument  \
    --SiteId site-eilhrmr2 \
    --FiberType SM \
    --OpticalStandard MM \
    --PowerConnectors 220VAC50HZ \
    --PowerFeedDrop UP \
    --MaxWeight 800 \
    --PowerDrawKva 5 \
    --UplinkSpeedGbps 10 \
    --UplinkCount 2 \
    --ConditionRequirement true \
    --DimensionRequirement true \
    --RedundantNetworking true \
    --NeedHelp true \
    --RedundantPower true \
    --BreakerRequirement true
```

Output: 
```
{
    "Response": {
        "RequestId": "3ceeecd2-2f24-4b3f-81eb-346137682c2f"
    }
}
```

