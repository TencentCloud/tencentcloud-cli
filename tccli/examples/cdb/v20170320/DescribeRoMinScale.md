**Example 1: 获取只读实例购买或升级的最小规格**



Input: 

```
tccli cdb DescribeRoMinScale --cli-unfold-argument  \
    --RoInstanceId cdbro-831kwfnh \
    --MasterInstanceId cdb-r66ityd5
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "Volume": 50,
        "Memory": 1000
    }
}
```

