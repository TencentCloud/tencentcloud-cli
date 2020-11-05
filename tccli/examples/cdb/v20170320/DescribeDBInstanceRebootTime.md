**Example 1: Querying the estimated restart time of TencentDB instance**



Input: 

```
tccli cdb DescribeDBInstanceRebootTime --cli-unfold-argument  \
    --InstanceIds cdb-f35wr6wj
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 1,
        "Items": [
            {
                "TimeInSeconds": 50,
                "InstanceId": "cdb-rozjda3j"
            }
        ]
    }
}
```

