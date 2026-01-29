**Example 1: 查询表**



Input: 

```
tccli tcb ListTables --cli-unfold-argument  \
    --MgoOffset 0 \
    --MgoLimit 20 \
    --Tag tnt-nl7hjzasw
```

Output: 
```
{
    "Response": {
        "RequestId": "4ce5365a-af8c-4859-a0dd-a4bfe1f2a3d8",
        "Tables": [
            {
                "TableName": "aris",
                "Count": 12,
                "Size": 899,
                "IndexCount": 1,
                "IndexSize": 36864
            },
            {
                "TableName": "test2",
                "Count": 1,
                "Size": 36,
                "IndexCount": 1,
                "IndexSize": 16384
            },
            {
                "TableName": "test3",
                "Count": 0,
                "Size": 0,
                "IndexCount": 1,
                "IndexSize": 4096
            },
            {
                "TableName": "test4",
                "Count": 0,
                "Size": 0,
                "IndexCount": 1,
                "IndexSize": 4096
            }
        ],
        "Pager": {
            "Offset": 0,
            "Limit": 20,
            "Total": 4
        }
    }
}
```

**Example 2: 查询表-使用MongoDB连接器**



Input: 

```
tccli tcb ListTables --cli-unfold-argument  \
    --MgoLimit 10 \
    --MgoOffset 0 \
    --Tag mongo_conn \
    --ShowHidden False \
    --EnvId lowcode-2gqvfid5936609f4 \
    --MongoConnector.InstanceId mongo_conn \
    --MongoConnector.DatabaseName demo_db
```

Output: 
```
{
    "Response": {
        "RequestId": "ee8f0898-b446-44cd-8773-676d8758c45c",
        "Pager": {
            "Offset": 0,
            "Limit": 10,
            "Total": 2
        },
        "Tables": [
            {
                "TableName": "demo_db",
                "Count": 0,
                "Size": 0,
                "IndexCount": 1,
                "IndexSize": 4096
            },
            {
                "TableName": "demo_users",
                "Count": 0,
                "Size": 0,
                "IndexCount": 2,
                "IndexSize": 8192
            }
        ]
    }
}
```

