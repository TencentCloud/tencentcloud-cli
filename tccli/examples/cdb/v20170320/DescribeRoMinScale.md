**Example 1: Querying the minimum specification of a read-only instance that can be purchased or upgraded to**



Input: 

```
tccli cdb DescribeRoMinScale --cli-unfold-argument  \
    --RoInstanceId cdbro-831kwfnh\
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

