**Example 1: 解隔离实例**

实例的解隔离操作。

Input: 

```
tccli postgres DisIsolateDBInstances --cli-unfold-argument  \
    --Period 1 \
    --AutoVoucher false \
    --DBInstanceIdSet postgres-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "ad1ca88b-5cc8-4c4c-ab10-a882123f8daa"
    }
}
```

