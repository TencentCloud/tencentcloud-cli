**Example 1: 创建配额告警**



Input: 

```
tccli quota CreateAlarm --cli-unfold-argument  \
    --Name 配额2 \
    --ProductId 2 \
    --QuotaId 3 \
    --Metrics 1 \
    --Threshold 1 \
    --Frequency 1
```

Output: 
```
{
    "Response": {
        "AlarmId": 119,
        "RequestId": "573f1a99-3b45-40bd-8c63-fdd311e1998e"
    }
}
```

