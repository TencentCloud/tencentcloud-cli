**Example 1: 创建备份**

创建备份

Input: 

```
tccli sqlserver CreateBackup --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl \
    --Strategy 1 \
    --DBNames db1 db2
```

Output: 
```
{
    "Response": {
        "RequestId": "4be5990d-a4b5-49dc-b2b4-e713b6aa7ba3",
        "FlowId": 5293
    }
}
```

