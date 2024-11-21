**Example 1: 查询购买页可购买的实例规格**

该接口（DescribeInstanceSpecs）用于查询购买页可购买的实例规格

Input: 

```
tccli cynosdb DescribeInstanceSpecs --cli-unfold-argument  \
    --DbType MYSQL
```

Output: 
```
{
    "Response": {
        "InstanceSpecSet": [
            {
                "Cpu": 1,
                "Memory": 1,
                "MaxStorageSize": 1,
                "MinStorageSize": 1,
                "HasStock": true,
                "MachineType": "exclusive",
                "MaxIops": 0,
                "MaxIoBandWidth": 0,
                "ZoneStockInfos": [
                    {
                        "Zone": "ap-beijing-3",
                        "HasStock": true,
                        "StockCount": 0
                    }
                ],
                "StockCount": 0
            }
        ],
        "RequestId": "1c7f08d0-e143-4305-9554-ea236d1a2981"
    }
}
```

