**Example 1: 查询表信息**



Input: 

```
tccli tcb DescribeTable --cli-unfold-argument  \
    --TableName adisa \
    --Tag tnt-a5a7a8aeu
```

Output: 
```
{
    "Response": {
        "Indexes": [
            {
                "Name": "example-index-0",
                "Size": 16384,
                "Unique": false,
                "Keys": [
                    {
                        "Name": "key0",
                        "Direction": "1"
                    }
                ],
                "Accesses": {
                    "Ops": 0,
                    "Since": "2019-03-05T19:47:53.797+08:00"
                }
            },
            {
                "Name": "_id_",
                "Size": 36864,
                "Unique": true,
                "Keys": [
                    {
                        "Name": "_id",
                        "Direction": "1"
                    }
                ],
                "Accesses": {
                    "Ops": 0,
                    "Since": "2019-02-28T11:46:20.919+08:00"
                }
            }
        ],
        "IndexNum": 2,
        "RequestId": "b9872df9-b00e-497d-9fdd-33338f0f64b4"
    }
}
```

**Example 2: 查询表信息-使用MongoDB连接器**

查询连接器内的表信息

Input: 

```
tccli tcb DescribeTable --cli-unfold-argument  \
    --TableName luke_test \
    --EnvId lowcode-1g1ac0pjd4eca700 \
    --MongoConnector.InstanceId luke_test2 \
    --MongoConnector.DatabaseName adise
```

Output: 
```
{
    "Response": {
        "IndexNum": 2,
        "Indexes": [
            {
                "Accesses": {
                    "Ops": 0,
                    "Since": "2025-12-09T16:37:19.051+08:00"
                },
                "Keys": [
                    {
                        "Direction": "1",
                        "Name": "_id"
                    }
                ],
                "Name": "_id_",
                "Size": 36864,
                "Unique": false
            },
            {
                "Accesses": {
                    "Ops": 2,
                    "Since": "2025-12-09T16:37:19.083+08:00"
                },
                "Keys": [
                    {
                        "Direction": "1",
                        "Name": "_openid"
                    }
                ],
                "Name": "_openid_1",
                "Size": 36864,
                "Unique": false
            }
        ],
        "RequestId": "1c71e3a6-c0ef-411c-819a-5321e3480800"
    }
}
```

