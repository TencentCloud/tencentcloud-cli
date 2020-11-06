**Example 1: Modifying backup log retention days**



Input: 

```
tccli mariadb ModifyLogFileRetentionPeriod --cli-unfold-argument  \
    --InstanceId tdsql-ige1a5k3 \
    --Days 29
```

Output: 
```
{
    "Response": {
        "InstanceId": "tdsql-ige1a5k3",
        "RequestId": "7f642839-f40d-4faf-8d84-be7894ce048a"
    }
}
```

