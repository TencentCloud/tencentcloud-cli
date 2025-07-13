**Example 1: 标记风险或者告警为**



Input: 

```
tccli csip UpdateAccessKeyAlarmStatus --cli-unfold-argument  \
    --Status 0 \
    --RiskIDList 91000005
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Msg": "success",
        "RequestId": "2a8b1b1e-e8c7-4b5d-8674-6881faa18a96"
    }
}
```

