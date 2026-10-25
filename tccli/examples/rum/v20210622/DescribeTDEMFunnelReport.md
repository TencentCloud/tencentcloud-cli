**Example 1: 示例**



Input: 

```
tccli rum DescribeTDEMFunnelReport --cli-unfold-argument  \
    --AppId 1****7 \
    --FunnelId c746a247-4927-40b7-9a7e-8b16a3bda58 \
    --StartTime 1778574700198 \
    --EndTime 1779179500198 \
    --Platform web \
    --DeviceType desktop \
    --Browser Chrome \
    --OS Mac OS X \
    --Country 中国 \
    --Referrer unknown \
    --AppVersion 2.0.0
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "{\"Code\":\"ResourceNotFound\",\"Message\":\"漏斗不存在\"}",
        "RequestId": "344ca442-775f-4334-876d-2d451c3e7a43"
    }
}
```

