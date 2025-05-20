**Example 1: 扩容云硬盘参数转换**



Input: 

```
tccli lighthouse SwitchParameterResizeDisks --cli-unfold-argument  \
    --DiskIds lhdisk-jgszqvs0 \
    --DiskSize 40
```

Output: 
```
{
    "Response": {
        "DiskOrder": "{\"ownerUin\": \"700000164995\", \"uin\": \"700000164995\", \"appId\": 251202221, \"projectId\": 0, \"zoneId\": 300002, \"goods\": [{\"goodsCategoryId\": 1025096, \"payMode\": 1, \"regionId\": 5, \"goodsNum\": 1, \"action\": \"modify\", \"goodsDetail\": {\"resourceId\": \"lhdisk-jgszqvs0\", \"oldConfig\": {\"timeUnit\": \"m\", \"pid\": 1010456, \"productCode\": \"p_lighthouse\", \"subProductCode\": \"sp_lighthouse_disk\", \"diskType\": \"CLOUD_PREMIUM\", \"diskSize\": 20, \"operation\": \"ResizeDisks\", \"sv_lighthouse_disk_premium_01\": 20, \"signature\": \"d1c819a18e614e038ea8cd96f46c55cc\"}, \"newConfig\": {\"timeUnit\": \"m\", \"pid\": 1010456, \"productCode\": \"p_lighthouse\", \"subProductCode\": \"sp_lighthouse_disk\", \"diskType\": \"CLOUD_PREMIUM\", \"diskSize\": 40, \"operation\": \"ResizeDisks\", \"sv_lighthouse_disk_premium_01\": 40, \"signature\": \"40e20c0a8c823f7ac7ab96eab8eecb56\"}, \"curDeadline\": \"2023-12-10 11:14:26\", \"productInfo\": [{\"name\": \"云硬盘类型\", \"value\": \"数据盘\"}, {\"name\": \"云硬盘介质类型\", \"value\": \"高性能云硬盘\"}, {\"name\": \"云硬盘大小\", \"value\": \"40\"}, {\"name\": \"地域\", \"value\": \"中国香港\"}]}}]}",
        "RequestId": "1062704c-1e8e-445b-b283-b20c21b87012"
    }
}
```

