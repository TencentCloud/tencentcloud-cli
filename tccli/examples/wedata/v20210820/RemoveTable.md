**Example 1: 移除table元数据**

移除table元数据

Input: 

```
tccli wedata RemoveTable --cli-unfold-argument  \
    --DatasourceId 62112 \
    --DatabaseName default \
    --SchemaName default_schema \
    --TableName luffyshi_test3
```

Output: 
```
{
    "Response": {
        "RequestId": "a6eb792f-8190-4443-94b3-976fbc2d95bc",
        "Result": true
    }
}
```

