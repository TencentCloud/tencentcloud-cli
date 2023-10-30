**Example 1: 计量设置余量阈值**



Input: 

```
tccli billing ModifyMeasureResourceAlarmThreshold --cli-unfold-argument  \
    --ProductCode p_rav \
    --ResourceId 100052301 \
    --Thresholds 50
```

Output: 
```
{
    "Response": {
        "RequestId": "95577512-8a64-4f38-a770-45d3a8bd6be7"
    }
}
```

