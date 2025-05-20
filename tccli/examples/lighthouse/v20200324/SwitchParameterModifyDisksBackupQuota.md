**Example 1: 调整云硬盘备份点配额参数转换**



Input: 

```
tccli lighthouse SwitchParameterModifyDisksBackupQuota --cli-unfold-argument  \
    --DiskIds lhdisk-guzg7nsa \
    --DiskBackupQuota 4
```

Output: 
```
{
    "Response": {
        "DiskOrder": "{\"ownerUin\": \"700000164995\", \"uin\": \"700000164995\", \"appId\": 251202221, \"projectId\": 0, \"zoneId\": 300002, \"goods\": [{\"goodsCategoryId\": 1025096, \"payMode\": 1, \"regionId\": 5, \"goodsNum\": 1, \"action\": \"modify\", \"goodsDetail\": {\"resourceId\": \"lhdisk-guzg7nsa\", \"oldConfig\": {\"timeUnit\": \"m\", \"pid\": 1010456, \"productCode\": \"p_lighthouse\", \"subProductCode\": \"sp_lighthouse_disk\", \"sv_lighthouse_disk_premium_01\": 20, \"diskType\": \"CLOUD_PREMIUM\", \"diskSize\": 20, \"operation\": \"ModifyDisksBackupQuota\", \"diskBackupQuota\": 3, \"sv_lighthouse_disk_backup_storage_general\": 60, \"signature\": \"b892d477d3a5a63b74b248d05c773690\"}, \"newConfig\": {\"timeUnit\": \"m\", \"pid\": 1010456, \"productCode\": \"p_lighthouse\", \"subProductCode\": \"sp_lighthouse_disk\", \"sv_lighthouse_disk_premium_01\": 20, \"diskType\": \"CLOUD_PREMIUM\", \"diskSize\": 20, \"diskBackupQuota\": 4, \"sv_lighthouse_disk_backup_storage_general\": 80, \"operation\": \"ModifyDisksBackupQuota\", \"signature\": \"bd0ebd56c1f78cb8bc38177b774c46f3\"}, \"curDeadline\": \"2023-10-22 12:20:03\", \"productInfo\": [{\"name\": \"云硬盘类型\", \"value\": \"数据盘\"}, {\"name\": \"云硬盘介质类型\", \"value\": \"高性能云硬盘\"}, {\"name\": \"云硬盘大小\", \"value\": \"20\"}, {\"name\": \"地域\", \"value\": \"中国香港\"}, {\"name\": \"云硬盘备份点配额\", \"value\": \"4\"}]}}]}",
        "RequestId": "822edbc4-5d4a-4e19-9d61-2a243f04d06e"
    }
}
```

