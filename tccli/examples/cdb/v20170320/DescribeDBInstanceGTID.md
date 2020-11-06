**Example 1: Querying whether GTID is activated for a TencentDB instance**



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

