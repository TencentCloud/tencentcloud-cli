**Example 1: 根据操作类型查询实例规格**



Input: 

```
tccli cynosdb DescribeInstanceSpecsByOperationType --cli-unfold-argument  \
    --ClusterId abc \
    --InstanceId abc \
    --OperationType abc
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
                "MachineType": "abc",
                "MaxIops": 0,
                "MaxIoBandWidth": 0,
                "ZoneStockInfos": [
                    {
                        "Zone": "abc",
                        "HasStock": true,
                        "StockCount": 0
                    }
                ],
                "StockCount": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

