**Example 1: 获取table列表**



Input: 

```
tccli cynosdb DescribeClusterDatabaseTables --cli-unfold-argument  \
    --Db xxx \
    --ClusterId xxx
```

Output: 
```
{
    "Response": {
        "Tables": [
            "testtable"
        ],
        "Limit": 20,
        "Offset": 0,
        "RequestId": "198189",
        "TotalCount": 1
    }
}
```

