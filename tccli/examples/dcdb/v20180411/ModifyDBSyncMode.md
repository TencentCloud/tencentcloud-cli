**Example 1: Modifying the sync mode of a TencentDB instance**



Input: 

```
tccli dcdb ModifyDBSyncMode --cli-unfold-argument  \
    --InstanceId dcdbt-avw0207d \
    --SyncMode 0
```

Output: 
```
{
    "Response": {
        "RequestId": "901bd41c-08a2-4001-8364-5a63f32056ae",
        "FlowId": 3521
    }
}
```

