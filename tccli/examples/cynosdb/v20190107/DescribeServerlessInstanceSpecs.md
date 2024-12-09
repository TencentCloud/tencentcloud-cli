**Example 1: 查询Serverless实例可选规格**



Input: 

```
tccli cynosdb DescribeServerlessInstanceSpecs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Specs": [
            {
                "MaxStorageSize": 1000,
                "MinCpu": 0.25,
                "StockCount": 0,
                "MaxCpu": 0.5,
                "HasStock": true,
                "IsDefault": 0
            },
            {
                "MaxStorageSize": 1000,
                "MinCpu": 0.25,
                "StockCount": 0,
                "MaxCpu": 0.0,
                "HasStock": true,
                "IsDefault": 0
            },
            {
                "MaxStorageSize": 5000,
                "MinCpu": 0.25,
                "StockCount": 0,
                "MaxCpu": 0.0,
                "HasStock": true,
                "IsDefault": 0
            },
            {
                "MaxStorageSize": 10000,
                "MinCpu": 0.25,
                "StockCount": 0,
                "MaxCpu": 0.0,
                "HasStock": true,
                "IsDefault": 0
            },
            {
                "MaxStorageSize": 1000,
                "MinCpu": 0.5,
                "StockCount": 0,
                "MaxCpu": 0.0,
                "HasStock": true,
                "IsDefault": 0
            },
            {
                "MaxStorageSize": 5000,
                "MinCpu": 0.5,
                "StockCount": 0,
                "MaxCpu": 0.0,
                "HasStock": true,
                "IsDefault": 1
            },
            {
                "MaxStorageSize": 10000,
                "MinCpu": 0.5,
                "StockCount": 0,
                "MaxCpu": 0.0,
                "HasStock": true,
                "IsDefault": 0
            },
            {
                "MaxStorageSize": 5000,
                "MinCpu": 0.0,
                "StockCount": 0,
                "MaxCpu": 0.0,
                "HasStock": true,
                "IsDefault": 0
            },
            {
                "MaxStorageSize": 10000,
                "MinCpu": 0.0,
                "StockCount": 0,
                "MaxCpu": 0.0,
                "HasStock": true,
                "IsDefault": 0
            },
            {
                "MaxStorageSize": 10000,
                "MinCpu": 0.0,
                "StockCount": 0,
                "MaxCpu": 0.0,
                "HasStock": true,
                "IsDefault": 0
            }
        ],
        "RequestId": "52-a341-4269-bce2-221ec952ea16|m"
    }
}
```

