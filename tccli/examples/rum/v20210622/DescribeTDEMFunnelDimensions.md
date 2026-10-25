**Example 1: 示例**



Input: 

```
tccli rum DescribeTDEMFunnelDimensions --cli-unfold-argument  \
    --AppId 1****7 \
    --FunnelId c746a2b16a3bda58e \
    --StartTime 1778574700198 \
    --EndTime 1779179500198 \
    --Dimension os \
    --Platform web \
    --DeviceType desktop \
    --Browser Chrome \
    --OS Max OS X \
    --Country 中国 \
    --Referrer unknown \
    --AppVersion 2.0.0
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "{\"Code\":\"ResourceNotFound\",\"Message\":\"漏斗不存在\"}",
        "RequestId": "daa50b58-793a-4c55-bc04-3b583cf08d68"
    }
}
```

