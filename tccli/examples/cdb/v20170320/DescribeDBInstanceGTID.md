**Example 1: 查询云数据实例的GTID是否开通**



Input: 

```
tccli cdb DescribeDBInstanceGTID --cli-unfold-argument  \
    --InstanceId cdb-f35wr6wj
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "IsGTIDOpen": 1
    }
}
```

