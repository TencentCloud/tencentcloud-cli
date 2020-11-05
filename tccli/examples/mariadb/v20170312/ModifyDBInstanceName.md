**Example 1: Renaming instance**



Input: 

```
tccli mariadb ModifyDBInstanceName --cli-unfold-argument  \
    --InstanceId tdsql-fdpjf5zh\
    --InstanceName newname
```

Output: 
```
{
    "Response": {
        "RequestId": "6a6b0cc7-c183-4e50-bf19-b83aa9fe77fc",
        "InstanceId": "tdsql-fdpjf5zh"
    }
}
```

