**Example 1: 解隔离实例**



Input: 

```
tccli postgres DisIsolateDBInstances --cli-unfold-argument  \
    --DBInstanceIdSet postgres-xxxxxxxx \
    --Period 1 \
    --AutoVoucher false
```

Output: 
```
{
    "Response": {
        "RequestId": "ad1ca88b-5cc8-4c4c-ab10-a882123f8daa"
    }
}
```

