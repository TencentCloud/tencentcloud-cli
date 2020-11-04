**Example 1: 请求示例**



Input: 

```
tccli redis ModifyAutoBackupConfig --cli-unfold-argument  \
    --InstanceId crs-5a4py64p\
    --TimePeriod 00%3A00-01%3A00\
    --AutoBackupType 1\
    --WeekDays Wednesday
```

Output: 
```
{
    "Response": {
        "AutoBackupType": 1,
        "WeekDays": [
            "Wednesday"
        ],
        "TimePeriod": "00:00-01:00",
        "RequestId": "ac750a85-9a55-4a42-a9de-8c2ca1f4ff12"
    }
}
```

