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
        "RequestId": "114114",
        "InstanceSpecSet": [
            {
                "MinStorageSize": 100,
                "MaxStorageSize": 100,
                "Cpu": 2,
                "Memory": 4
            },
            {
                "MinStorageSize": 100,
                "MaxStorageSize": 100,
                "Cpu": 4,
                "Memory": 8
            }
        ]
    }
}
```

