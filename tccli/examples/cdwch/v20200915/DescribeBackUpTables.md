**Example 1: 示例**



Input: 

```
tccli cdwch DescribeBackUpTables --cli-unfold-argument  \
    --InstanceId xx
```

Output: 
```
{
    "Response": {
        "AvailableTables": [
            {
                "Table": "xx",
                "VCluster": "xx",
                "TotalBytes": 0,
                "Database": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

