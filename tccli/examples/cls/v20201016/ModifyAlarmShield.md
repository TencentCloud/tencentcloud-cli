**Example 1: 修改告警屏蔽**

修改告警屏蔽

Input: 

```
tccli cls ModifyAlarmShield --cli-unfold-argument  \
    --TaskId bb42f112-a74d-456e-b3c4-ff5472911b42 \
    --AlarmNoticeId notice-bb42f112-a74d-456e-b3c4-ff5472911b42 \
    --StartTime 1701872657 \
    --EndTime 1701892657 \
    --Type 1 \
    --Rule  \
    --Reason 修改原因
```

Output: 
```
{
    "Response": {
        "RequestId": "1142f112-a74d-456e-b3c4-ff5472911b11"
    }
}
```

