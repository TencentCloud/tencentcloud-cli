**Example 1: 1**



Input: 

```
tccli tdmysql DescribeDatabaseObjects --cli-unfold-argument  \
    --InstanceId tdsql3-01d1c3ed \
    --DbName sys
```

Output: 
```
{
    "Response": {
        "DbName": "mysql",
        "Funcs": null,
        "InstanceId": "tdsql3-01d1c3ed",
        "Procs": null,
        "RequestId": "0e864abd-7dbb-468c-bbd0-fe8346bfdaf2",
        "Tables": [
            {
                "Table": "memory_global_by_current_bytes"
            }
        ],
        "Views": null
    }
}
```

