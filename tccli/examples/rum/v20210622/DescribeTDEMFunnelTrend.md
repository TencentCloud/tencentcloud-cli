**Example 1: 示例**



Input: 

```
tccli rum DescribeTDEMFunnelTrend --cli-unfold-argument  \
    --AppId 1****7 \
    --FunnelId c746a247-4927-40b7-9a7e-8b16a3bda58 \
    --StartTime 1778574700198 \
    --EndTime 1779179500198 \
    --Interval day \
    --Platform web \
    --AppVersion 2.0.0 \
    --DeviceType desktop \
    --Browser Chrome \
    --OS Mac OS X \
    --Country 中国 \
    --Referrer 页面来源
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "{\"Code\":\"ResourceNotFound\",\"Message\":\"漏斗不存在\"}",
        "RequestId": "de184bb1-7941-4447-afb7-3370fa5b151c"
    }
}
```

