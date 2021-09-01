**Example 1: 创建数据库test_db**



Input: 

```
tccli sqlserver CreateDB --cli-unfold-argument  \
    --InstanceId mssql-i1z41iwd \
    --DBs.0.DBName test_db \
    --DBs.0.Charset Chinese_PRC_CI_AS
```

Output: 
```
{
    "Response": {
        "FlowId": 123,
        "RequestId": "4be5990d-a4b5-49dc-b2b4-e713b6aa7ba3"
    }
}
```

