**Example 1: 新购云硬盘下单参数转换**

新购云硬盘下单参数转换

Input: 

```
tccli lighthouse SwitchParameterCreateDisks --cli-unfold-argument  \
    --DiskSize 50 \
    --DiskType CLOUD_PREMIUM \
    --DiskCount 1 \
    --DiskName testName \
    --Zone ap-hongkong-2 \
    --DiskChargePrepaid.Period 1 \
    --DiskBackupQuota 1
```

Output: 
```
{
    "Response": {
        "DiskOrder": "{\"ownerUin\": \"800000294207\", \"uin\": \"800000294207\", \"appId\": 251221987, \"projectId\": 0, \"goods\": [{\"goodsCategoryId\": 102849, \"goodsNum\": 1, \"goodsDetail\": {\"pid\": 1010456, \"productCode\": \"p_lighthouse\", \"subProductCode\": \"sp_lighthouse_disk\", \"productInfo\": [{\"name\": \"云硬盘类型\", \"value\": \"数据盘\"}, {\"name\": \"云硬盘介质类型\", \"value\": \"高性能云硬盘\"}, {\"name\": \"云硬盘大小\", \"value\": \"50\"}, {\"name\": \"地域\", \"value\": \"中国香港\"}, {\"name\": \"云硬盘备份点配额\", \"value\": \"1\"}], \"sv_lighthouse_disk_premium_01\": 50, \"diskBackupQuota\": 1, \"sv_lighthouse_disk_backup_storage_general\": 50, \"autoRenewFlag\": 0, \"timeUnit\": \"m\", \"timeSpan\": 1, \"zone\": \"ap-hongkong-2\", \"diskSize\": 50, \"diskType\": \"CLOUD_PREMIUM\", \"intl\": false, \"diskName\": \"test\", \"signature\": \"fe7f80004b46385bc76be7089c547fe3\"}, \"regionId\": 5, \"payMode\": 1}], \"zoneId\": 300002}",
        "RequestId": "509029a2-b4cf-4f7a-9285-b24492b1fe29"
    }
}
```

