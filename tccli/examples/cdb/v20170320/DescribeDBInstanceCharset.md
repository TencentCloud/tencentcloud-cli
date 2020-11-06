**Example 1: Querying the character set of a TencentDB instance**



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

