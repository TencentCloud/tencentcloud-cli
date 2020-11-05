**Example 1: Modifies the project to which instances belong**



Input: 

```
tccli sqlserver ModifyDBInstanceProject --cli-unfold-argument  \
    --InstanceIdSet mssql-j8kv137v\
    --ProjectId 347
```

Output: 
```
{
    "Response": {
        "RequestId": "4be5990d-a4b5-49dc-b2b4-e713b6aa7ba3",
        "Count": 1
    }
}
```

