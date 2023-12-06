**Example 1: 更新预聚合规则**



Input: 

```
tccli monitor UpdateRecordingRule --cli-unfold-argument  \
    --InstanceId prom-xrwerwe \
    --RuleState 2 \
    --Group LS0tDQpuYW1lOiBleGFtcGxlDQpydWxlczoNCiAgLSByZWNvcmQ6IGpvYjpodHRwX2lucHJvZ3Jlc3NfcmVxdWVzdHM6c3VtDQogICAgZXhwcjogc3VtIGJ5IChqb2IpIChodHRwX2lucHJvZ3Jlc3NfcmVxdWVzdHMp \
    --Name test \
    --RuleId rrule-m74lrt6g
```

Output: 
```
{
    "Response": {
        "RequestId": "1z5ph-pcsxjbfy1y56525v5q-w5brnte",
        "RuleId": "rrule-m74lrt6g"
    }
}
```

