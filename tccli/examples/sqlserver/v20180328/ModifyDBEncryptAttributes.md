**Example 1: 开启、关闭数据库的TDE加密功能**

开启、关闭数据库的TDE加密功能

Input: 

```
tccli sqlserver ModifyDBEncryptAttributes --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl \
    --DBTDEEncrypt.0.DBName test_db \
    --DBTDEEncrypt.0.Encryption enable
```

Output: 
```
{
    "Response": {
        "FlowId": 1778292,
        "RequestId": "5062de55-d048-4d3b-92f9-b98b6f244360"
    }
}
```

