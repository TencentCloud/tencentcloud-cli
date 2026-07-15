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
        "SlowLogThreshold": 1000,
        "DrReadableInfo": {
            "DrInstanceId": "mssqldr-oo1",
            "Zone": "ap-guangzhou",
            "RoWeight": 0,
            "ReadableStatus": "",
            "ReadMode": "BalancedReadOnly",
            "SlaveStatus": "",
            "UniqSubnetId": "",
            "UniqVpcId": "",
            "VPort": 0,
            "Vip": ""
        },
        "EventSaveDays": 7,
        "InstanceId": "mssql-9pk12q33",
        "OldVipList": [],
        "RegularBackupCounts": 100,
        "RegularBackupEnable": "disable",
        "RegularBackupSaveDays": 123,
        "RegularBackupStartTime": "2024-06-17",
        "RegularBackupStrategy": "years",
        "RequestId": "c1bd8e12-4744-4d95-b08e-fbc2d8477c11",
        "SSLConfig": {
            "Encryption": "disable",
            "SSLValidity": 0,
            "SSLValidityPeriod": "0000-00-00 00:00:00"
        },
        "TDEConfig": {
            "CertificateAttribution": "none",
            "Encryption": "disable",
            "QuoteUin": ""
        },
        "XEventStatus": "disable",
        "MultiDrReadableInfo": [
            {
                "DrInstanceId": "mssqldr-jia78a",
                "Zone": "ap-guangzhou-3",
                "SlaveStatus": "DR_RUNNING",
                "ReadableStatus": "disable",
                "ReadMode": "BalancedReadOnly",
                "Vip": "",
                "VPort": 1433,
                "UniqVpcId": "",
                "UniqSubnetId": "",
                "RoWeight": 1
            }
        ]
    }
}
```

