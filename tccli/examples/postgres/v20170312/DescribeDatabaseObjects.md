**Example 1: 查询对象为database**

查询数据库列表

Input: 

```
tccli postgres DescribeDatabaseObjects --cli-unfold-argument  \
    --DBInstanceId postgres-5cz25tr5 \
    --ObjectType database
```

Output: 
```
{
    "Response": {
        "ObjectSet": [
            "postgres",
            "postgres_bak_1715170243",
            "user_database"
        ],
        "TotalCount": 3,
        "RequestId": "c90f7a9d-f519-4d2f-bb2f-e3966cd102b6"
    }
}
```

**Example 2: 查询对象为schema**

查询user_database下的模式

Input: 

```
tccli postgres DescribeDatabaseObjects --cli-unfold-argument  \
    --DBInstanceId postgres-5cz25tr5 \
    --ObjectType schema \
    --Limit 2 \
    --Offset 1 \
    --DatabaseName user_database
```

Output: 
```
{
    "Response": {
        "ObjectSet": [
            "information_schema",
            "pg_catalog"
        ],
        "TotalCount": 2,
        "RequestId": "bb6146b9-0c63-40ea-b89a-d83944805b79"
    }
}
```

**Example 3: 查询对象为table**

查询user_database数据库下，属于user_schema模式的表

Input: 

```
tccli postgres DescribeDatabaseObjects --cli-unfold-argument  \
    --DBInstanceId postgres-5cz25tr5 \
    --ObjectType table \
    --DatabaseName user_database \
    --SchemaName user_schema
```

Output: 
```
{
    "Response": {
        "ObjectSet": [
            "users",
            "users1",
            "users2"
        ],
        "TotalCount": 3,
        "RequestId": "80530420-d73e-4a60-8149-93cf800220b9"
    }
}
```

