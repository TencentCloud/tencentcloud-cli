**Example 1: Querying the sync mode of a TencentDB instance**



Input: 

```
tccli dcdb DescribeDBSyncMode --cli-unfold-argument  \
    --InstanceId dcdbt-avw0207d
```

Output: 
```
{
    "Response": {
        "RequestId": "901bd41c-08a2-4001-8364-5a63f32056ae",
        "SyncMode": 0,
        "IsModifying": 1
    }
}
```

