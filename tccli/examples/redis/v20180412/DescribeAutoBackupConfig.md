**Example 1: 请求示例**

查询指定实例的自动备份规则

Input: 

```
tccli redis DescribeAutoBackupConfig --cli-unfold-argument  \
    --InstanceId crs-5a4p****
```

Output: 
```
{
    "Response": {
        "RequestId": "65e950b9-78e8-49b1-9200-0e62a1925559",
        "BackupStorageDays": 7,
        "BinlogStorageDays": 7,
        "AutoBackupType": 1,
        "WeekDays": [
            "Monday",
            "Tuesday"
        ],
        "TimePeriod": "01:00-02:00"
    }
}
```

