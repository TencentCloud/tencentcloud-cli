**Example 1: 拉取数据库列表**

拉取数据库列表

Input: 

```
tccli postgres DescribeDatabases --cli-unfold-argument  \
    --DBInstanceId postgres-6bwgamo3
```

Output: 
```
{
    "Response": {
        "RequestId": "86eb714c-500f-412e-8090-3b3f76843d86",
        "Items": [
            "postgres",
            "testdatabase"
        ]
    }
}
```

