**Example 1: 查询云数据库实例的备份时间窗口配置**



Input: 

```
tccli mariadb DescribeBackupTime --cli-unfold-argument  \
    --InstanceIds tdsql-fdpjf5zh
```

Output: 
```
{
    "Response": {
        "RequestId": "caca6ca7-9ef0-48e0-aa7a-4327a1ac001c",
        "TotalCount": 1,
        "Items": [
            {
                "InstanceId": "tdsql-33y5ai5p",
                "StartBackupTime": "00:00",
                "EndBackupTime": "23:59"
            }
        ]
    }
}
```

