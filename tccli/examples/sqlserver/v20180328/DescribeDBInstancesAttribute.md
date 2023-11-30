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
        "BlockedThreshold": 0,
        "EventSaveDays": 7,
        "InstanceId": "mssql-j8kv137v",
        "RegularBackupCounts": 0,
        "RegularBackupEnable": "disable",
        "RegularBackupSaveDays": 0,
        "RegularBackupStartTime": "",
        "RegularBackupStrategy": "months",
        "RequestId": "9db13c19-d660-43c4-b340-7ba86b7b1470",
        "SSLConfig": {
            "Encryption": "disable",
            "SSLValidity": 0,
            "SSLValidityPeriod": "0000-00-00 00:00:00"
        },
        "TDEConfig": {
            "CertificateAttribution": "self",
            "Encryption": "disable",
            "QuoteUin": ""
        }
    }
}
```

