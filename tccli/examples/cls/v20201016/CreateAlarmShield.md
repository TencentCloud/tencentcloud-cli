**Example 1: 创建告警屏蔽**

创建告警屏蔽

Input: 

```
tccli cls CreateAlarmShield --cli-unfold-argument  \
    --AlarmNoticeId notice-bb42f112-a74d-456e-b3c4-ff5472911b42 \
    --StartTime 1701872657 \
    --EndTime 1701883657 \
    --Type 1 \
    --Rule  \
    --Reason 系统发布，暂时屏蔽
```

Output: 
```
{
    "Response": {
        "TaskId": "bb42f112-a74d-456e-b3c4-ff5472911b42",
        "RequestId": "1142f112-a74d-456e-b3c4-ff5472911b11"
    }
}
```

