**Example 1: 查询预聚合规则**



Input: 

```
tccli monitor DescribeRecordingRules --cli-unfold-argument  \
    --InstanceId prom-sdf342 \
    --RuleState 2 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RecordingRuleSet": [
            {
                "RuleId": "rrule-45hkgiyc",
                "RuleState": 2,
                "Name": "example6",
                "Group": "LS0tDQpuYW1lOiBleGFtcGxlDQpydWxlczoNCiAgLSByZWNvcmQ6IGpvYjpodHRwX2lucHJvZ3Jlc3NfcmVxdWVzdHM6c3VtDQogICAgZXhwcjogc3VtIGJ5IChqb2IpIChodHRwX2lucHJvZ3Jlc3NfcmVxdWVzdHMp",
                "Total": 1,
                "UpdatedAt": "2020-08-10T17:50:06Z",
                "CreatedAt": "2020-08-10T09:32:51Z"
            }
        ],
        "RequestId": "-1y24pm54antkuiziyii7hxwv2974riq",
        "TotalCount": 1
    }
}
```

