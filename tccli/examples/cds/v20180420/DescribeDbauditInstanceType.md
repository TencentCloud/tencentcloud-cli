**Example 1: 查询产品规格信息列表**

本示例用于查询数据安全审计产品规格信息列表

Input: 

```
tccli cds DescribeDbauditInstanceType --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7",
        "DbauditTypesSet": [
            {
                "InstanceVersionName": "合规版",
                "InstanceVersionKey": "cdsaudit",
                "Qps": "3000",
                "MaxInstances": 3,
                "InsertSpeed": 3000000,
                "OnlineStorageCapacity": 400000000,
                "ArchivingStorageCapacity": 4000000000
            },
            {
                "InstanceVersionName": "高级版",
                "InstanceVersionKey": "cdsaudit_adv",
                "Qps": "3000",
                "MaxInstances": 6,
                "InsertSpeed": 3000000,
                "OnlineStorageCapacity": 400000000,
                "ArchivingStorageCapacity": 4000000000
            }
        ]
    }
}
```

