**Example 1: 查询可售卖实例规格信息**



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
                "MaxStorageSize": 1,
                "ZoneStockInfos": [
                    {
                        "HasStock": true,
                        "Zone": "xx"
                    }
                ],
                "MachineType": "xx",
                "HasStock": true,
                "Memory": 1,
                "MinStorageSize": 1,
                "MaxIoBandWidth": 0,
                "Cpu": 1,
                "MaxIops": 0
            },
            {
                "MaxStorageSize": 1,
                "ZoneStockInfos": [
                    {
                        "HasStock": true,
                        "Zone": "xx"
                    }
                ],
                "MachineType": "xx",
                "HasStock": true,
                "Memory": 1,
                "MinStorageSize": 1,
                "MaxIoBandWidth": 0,
                "Cpu": 1,
                "MaxIops": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

