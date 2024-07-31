**Example 1: 示例**



Input: 

```
tccli cdwdoris DescribeBackUpTables --cli-unfold-argument  \
    --InstanceId cdwdoris-123
```

Output: 
```
{
    "Response": {
        "AvailableTables": [
            {
                "Table": "tablename1",
                "TotalBytes": 0,
                "Database": "db1"
            }
        ],
        "RequestId": "request1"
    }
}
```

