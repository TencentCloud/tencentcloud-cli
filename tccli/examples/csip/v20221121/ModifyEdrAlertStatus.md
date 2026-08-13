**Example 1: 修改EDR告警状态**



Input: 

```
tccli csip ModifyEdrAlertStatus --cli-unfold-argument  \
    --Targets.0.Id 1000000000000580 \
    --Targets.0.AlertId ed7ba2b9a95370778b2a589412f655aa \
    --Targets.0.AppId 260108008 \
    --Targets.0.Quuid 11c73bc2-6918-4457-88d3-1c22ef2de87b \
    --Targets.0.InstanceId ins-h0zrmp36 \
    --Targets.0.AlertSubType BRUTE_FORCE \
    --Status PROCESSED
```

Output: 
```
{
    "Response": {
        "RequestId": "64834984-d8d5-4b92-8212-2bb1bf0bb4ad"
    }
}
```

