**Example 1: 查询云数据库实例的字符集**



Input: 

```
tccli cdb DescribeDBInstanceCharset --cli-unfold-argument  \
    --InstanceId cdb-f35wr6wj
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "Charset": "latin1"
    }
}
```

