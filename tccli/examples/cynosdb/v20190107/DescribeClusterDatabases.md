**Example 1: 获取集群数据库列表**



Input: 

```
tccli cynosdb DescribeClusterDatabases --cli-unfold-argument  \
    --ClusterId cynosdbmysql-tsjwe7iu
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "Limit": 20,
        "Offset": 0,
        "RequestId": "806fe1c8-5567-4aa8-a521-ea2414c793b4",
        "Databases": [
            "test_database_1",
            "test_database_2"
        ]
    }
}
```

