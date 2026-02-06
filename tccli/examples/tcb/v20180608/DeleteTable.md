**Example 1: 删除表**

使用环境内默认连接器

Input: 

```
tccli tcb DeleteTable --cli-unfold-argument  \
    --TableName adise \
    --Tag tnt-nl7hjzasw
```

Output: 
```
{
    "Response": {
        "RequestId": "5a54946c-0b9f-4dd7-b354-b0dc49185517"
    }
}
```

**Example 2: 删除表-使用MongoDB连接器**



Input: 

```
tccli tcb DeleteTable --cli-unfold-argument  \
    --TableName demo_users \
    --Tag mongo_conn \
    --EnvId lowcode-2gqvfid5936609f4 \
    --MongoConnector.InstanceId mongo_conn \
    --MongoConnector.DatabaseName demo_db
```

Output: 
```
{
    "Response": {
        "RequestId": "9a8dae16-1625-48ca-a409-535ccdb14fce"
    }
}
```

