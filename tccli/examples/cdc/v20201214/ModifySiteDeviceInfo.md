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
    --ConditionRequirement True \
    --DimensionRequirement True \
    --RedundantNetworking True \
    --NeedHelp True \
    --RedundantPower True \
    --BreakerRequirement True
```

Output: 
```
{
    "Response": {
        "RequestId": "3ceeecd2-2f24-4b3f-81eb-346137682c2f"
    }
}
```

