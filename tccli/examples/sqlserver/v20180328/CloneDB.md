**Example 1: 克隆数据库**



Input: 

```
tccli sqlserver CloneDB --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl \
    --RenameRestore.0.OldName db1 \
    --RenameRestore.0.NewName clone_db1
```

Output: 
```
{
    "Response": {
        "RequestId": "4be5990d-a4b5-49dc-b2b4-e713b6aa7ba3",
        "FlowId": 3546
    }
}
```

