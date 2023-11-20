**Example 1: 将实例mssql-njj2mtpl备注修改为noteMsg**



Input: 

```
tccli sqlserver ModifyDBInstanceNote --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl \
    --InstanceNote noteMsg
```

Output: 
```
{
    "Response": {
        "RequestId": "8a61e500-aa33-454c-9ec2-da2a368c39ab"
    }
}
```

