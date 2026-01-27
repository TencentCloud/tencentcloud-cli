**Example 1: 查询遗留备份集群信息**

Describe Save Backup Clusters

Input: 

```
tccli cynosdb DescribeSaveBackupClusters --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "3885b16b-9a20-4a56-8c01-688f7e69a4f1",
        "SaveBackupClusterInfos": [
            {
                "BackupId": 0,
                "BackupTime": "0001-01-01 00:00:00",
                "ClusterId": "cynosdbmysql-2e9qy0ob",
                "ClusterName": "cynosdbmysql-2e9qy0ob",
                "DbMode": "NORMAL",
                "DbVersion": "5.7",
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-3"
            }
        ],
        "TotalCount": 2
    }
}
```

