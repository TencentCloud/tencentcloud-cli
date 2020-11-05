**Example 1: Renaming the instance mssql-njj2mtpl to testModifyInstanceName**



Input: 

```
tccli sqlserver ModifyDBInstanceName --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl\
    --InstanceName testModifyInstanceName
```

Output: 
```
{
    "Response": {
        "RequestId": "8a61e500-aa33-454c-9ec2-da2a368c39ab"
    }
}
```

