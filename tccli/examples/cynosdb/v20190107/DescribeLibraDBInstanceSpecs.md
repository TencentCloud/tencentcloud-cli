**Example 1: 查询只读分析引擎在该地域支持的规格列表信息**

本接口(DescribeLibraDBInstanceSpecs)用于查询只读分析引擎在该地域支持的规格列表信息

Input: 

```
tccli cynosdb DescribeLibraDBInstanceSpecs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "InstanceSpecSet": [
            {
                "Cpu": 128,
                "HasStock": true,
                "InstanceType": "common",
                "MaxReplicaNum": 1,
                "MaxStorageSize": 15000,
                "Memory": 512,
                "MinReplicaNum": 1,
                "MinStorageSize": 100,
                "StorageType": "CLOUD_TCS",
                "ZoneStockInfos": []
            },
            {
                "Cpu": 4,
                "HasStock": true,
                "InstanceType": "common",
                "MaxReplicaNum": 1,
                "MaxStorageSize": 7000,
                "Memory": 16,
                "MinReplicaNum": 1,
                "MinStorageSize": 100,
                "StorageType": "CLOUD_TCS",
                "ZoneStockInfos": []
            },
            {
                "Cpu": 8,
                "HasStock": true,
                "InstanceType": "common",
                "MaxReplicaNum": 1,
                "MaxStorageSize": 7000,
                "Memory": 32,
                "MinReplicaNum": 1,
                "MinStorageSize": 100,
                "StorageType": "CLOUD_TCS",
                "ZoneStockInfos": []
            },
            {
                "Cpu": 16,
                "HasStock": true,
                "InstanceType": "common",
                "MaxReplicaNum": 1,
                "MaxStorageSize": 15000,
                "Memory": 64,
                "MinReplicaNum": 1,
                "MinStorageSize": 100,
                "StorageType": "CLOUD_TCS",
                "ZoneStockInfos": []
            },
            {
                "Cpu": 32,
                "HasStock": true,
                "InstanceType": "common",
                "MaxReplicaNum": 1,
                "MaxStorageSize": 15000,
                "Memory": 128,
                "MinReplicaNum": 1,
                "MinStorageSize": 100,
                "StorageType": "CLOUD_TCS",
                "ZoneStockInfos": []
            },
            {
                "Cpu": 64,
                "HasStock": true,
                "InstanceType": "common",
                "MaxReplicaNum": 1,
                "MaxStorageSize": 15000,
                "Memory": 256,
                "MinReplicaNum": 1,
                "MinStorageSize": 100,
                "StorageType": "CLOUD_TCS",
                "ZoneStockInfos": []
            },
            {
                "Cpu": 96,
                "HasStock": true,
                "InstanceType": "common",
                "MaxReplicaNum": 1,
                "MaxStorageSize": 15000,
                "Memory": 384,
                "MinReplicaNum": 1,
                "MinStorageSize": 100,
                "StorageType": "CLOUD_TCS",
                "ZoneStockInfos": []
            }
        ],
        "RequestId": "62071f40-549c-11ef-807f-195586da5700"
    }
}
```

