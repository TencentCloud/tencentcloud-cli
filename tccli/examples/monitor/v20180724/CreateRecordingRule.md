**Example 1: 创建预聚合规则**



Input: 

```
tccli monitor CreateRecordingRule --cli-unfold-argument  \
    --InstanceId prom-xxxxsfds \
    --RuleState 2 \
    --Group LS0tDQpuYW1lOiBleGFtcGxlDQpydWxlczoNCiAgLSByZWNvcmQ6IGpvYjpodHRwX2lucHJvZ3Jlc3NfcmVxdWVzdHM6c3VtDQogICAgZXhwcjogc3VtIGJ5IChqb2IpIChodHRwX2lucHJvZ3Jlc3NfcmVxdWVzdHMp \
    --Name 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xyz",
        "RuleId": "rrule-xyz"
    }
}
```

