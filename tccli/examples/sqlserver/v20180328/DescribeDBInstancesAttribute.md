**Example 1: 查询实例mssql-j8kv137v的附属属性**

查询实例附属属性

Input: 

```
tccli sqlserver DescribeDBInstancesAttribute --cli-unfold-argument  \
    --InstanceId mssql-j8kv137v
```

Output: 
```
{
    "Response": {
        "InstanceId": "mssql-j8kv137v",
        "RegularBackupSaveDays": 1,
        "RequestId": "7",
        "RegularBackupCounts": 1,
        "RegularBackupEnable": "enable",
        "RegularBackupStrategy": "months",
        "RegularBackupStartTime": "2022-10-10",
        "EventSaveDays": 0,
        "TDEConfig": {
            "Encryption": "disable",
            "CertificateAttribution": "self",
            "QuoteUin": ""
        },
        "BlockedThreshold": 6
    }
}
```

