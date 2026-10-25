**Example 1: 示例**



Input: 

```
tccli rum DescribeTDEMFunnelStepSessionList --cli-unfold-argument  \
    --AppId 146667 \
    --FunnelId 324 \
    --StartTime 1778574700198 \
    --EndTime 1779179500198 \
    --StepIndex 1 \
    --DrillType pass_through \
    --Page 1 \
    --PageSize 20 \
    --Platform web \
    --AppVersion 2.0.0 \
    --DeviceType desktop \
    --Browser Chrome \
    --OS Mac OS X \
    --Country 中国 \
    --Referrer unknown
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "{\"Code\":\"ResourceNotFound\",\"Message\":\"漏斗不存在\"}",
        "RequestId": "aaccceef-565d-40e8-8722-09d1c0bc6bf9"
    }
}
```

