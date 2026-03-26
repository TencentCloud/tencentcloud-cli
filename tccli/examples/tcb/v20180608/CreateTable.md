**Example 1: 新建表**



Input: 

```
tccli tcb CreateTable --cli-unfold-argument  \
    --TableName adsia \
    --Tag tnt-nl7hjzasw
```

Output: 
```
{
    "Response": {
        "RequestId": "C563943B-3BEA-FE92-29FE-591EAEB7871F"
    }
}
```

**Example 2: 新建表-使用MongoDB连接器**



Input: 

```
tccli tcb CreateTable --cli-unfold-argument  \
    --TableName demo_users \
    --Tag mongo_conn \
    --PermissionInfo.AclTag ADMINONLY \
    --PermissionInfo.EnvId lowcode-2gqvfid5936609f4 \
    --EnvId lowcode-2gqvfid5936609f4 \
    --MongoConnector.InstanceId mongo_conn \
    --MongoConnector.DatabaseName demo_db
```

Output: 
```
{
    "Response": {
        "RequestId": "1c42cd0e-0836-4b69-8bb0-204415b41a56"
    }
}
```

