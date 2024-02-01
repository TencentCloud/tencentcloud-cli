**Example 1: 搜索集群数据库列表**



Input: 

```
tccli cynosdb SearchClusterDatabases --cli-unfold-argument  \
    --ClusterId cynosdbmysql-qwer \
    --Database testDb
```

Output: 
```
{
    "Response": {
        "RequestId": "176466",
        "Databases": [
            "testDb"
        ]
    }
}
```

