**Example 1: Creating data import task**



Input: 

```
tccli cdb CreateDBImportJob --cli-unfold-argument  \
    --InstanceId cdb-ids6j1b3\
    --User xxxxx\
    --Password xxxxxxxxxx\
    --FileName test.sql
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "AsyncRequestId": "be9f64a6-fa652dc6-f5c878b6-a6a50746"
    }
}
```

