**Example 1: Dropping a database**



Input: 

```
tccli sqlserver DeleteDB --cli-unfold-argument  \
    --InstanceId mssql-rljoi3bf \
    --Names test_db
```

Output: 
```
{
    "Response": {
        "RequestId": "a928d733-109a-4f44-84ad-991da182d0a3",
        "FlowId": 30467
    }
}
```

