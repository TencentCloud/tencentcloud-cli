**Example 1: 获取集群数据库列表**



Input: 

```
tccli cynosdb DescribeClusterDatabases --cli-unfold-argument  \
    --ClusterId xxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "Limit": 20,
        "Offset": 1,
        "RequestId": "176466",
        "Databases": []
    }
}
```

