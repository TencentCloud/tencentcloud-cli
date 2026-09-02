**Example 1: ExecutePGSql**



Input: 

```
tccli tcb ExecutePGSql --cli-unfold-argument  \
    --EnvId lo**od*-*********10a94df \
    --Sql select * from pg_namespace
```

Output: 
```
{
    "Response": {
        "AffectedRows": 0,
        "Columns": [
            "oid"
        ],
        "ExecutionTimeMs": 8,
        "Rows": [
            "[\"99\",\"pg_toast\",\"10\",null]"
        ],
        "RequestId": "6907a086-5639-4c9d-89bf-66921dd1168e"
    }
}
```

