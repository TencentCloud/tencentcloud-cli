**Example 1: 修改用户告警配置**



Input: 

```
tccli teo ModifyAlarmConfig --cli-unfold-argument  \
    --Threshold 0 \
    --EntityList tencent.com \
    --IsDefault True \
    --ServiceType ddos \
    --ZoneId zone-28569s6od5na
```

Output: 
```
{
    "Response": {
        "RequestId": "435afebf-6e98-4224-ac43-33ad9ac9ef09"
    }
}
```

