**Example 1: 搜索集群数据表列表**



Input: 

```
tccli cynosdb SearchClusterTables --cli-unfold-argument  \
    --ClusterId cynosdbmysql-qwerasd \
    --Database testDb
```

Output: 
```
{
    "Response": {
        "RequestId": "176466",
        "Tables": []
    }
}
```

