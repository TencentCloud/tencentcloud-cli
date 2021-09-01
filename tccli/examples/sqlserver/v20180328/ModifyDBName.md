**Example 1: 修改数据库名**



Input: 

```
tccli sqlserver ModifyDBName --cli-unfold-argument  \
    --InstanceId mssql-i1z41iwd \
    --OldDBName test_db \
    --NewDBName test_db_newname
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

