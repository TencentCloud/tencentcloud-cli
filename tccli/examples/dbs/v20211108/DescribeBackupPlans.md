**Example 1: 查询备份计划列表**



Input: 

```
tccli dbs DescribeBackupPlans --cli-unfold-argument  \
    --Status running checkPass \
    --AccessType extranet \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AccessType": "extranet",
                "AutoRenewFlag": 1,
                "BackupMethod": "logical",
                "BackupPlanId": "dbs-testcloud",
                "BackupPlanName": "dbs-nametest",
                "CreateTime": "2022-03-15 17:49:31",
                "DatabaseType": "percona",
                "EnableIncrement": false,
                "ExpireTime": "2022-05-15 17:49:31",
                "InstanceClass": "micro",
                "OfflineTime": "2022-05-31 09:36:18",
                "PayType": "prePay",
                "Region": "ap-guangzhou",
                "SourceInfo": [
                    "1.0.0.10:8888"
                ],
                "Status": "isolated",
                "Tags": [
                    {
                        "TagKey": "key",
                        "TagValue": "v"
                    }
                ]
            }
        ],
        "TotalCount": 2,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

