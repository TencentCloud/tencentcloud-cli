**Example 1: 批量隔离实例**



Input: 

```
tccli tdmysql CancelIsolateDBInstances --cli-unfold-argument  \
    --InstanceIds tdsql3-d8fffc3c
```

Output: 
```
{
    "Response": {
        "SuccessInstanceIds": [
            "tdsql3-d8fffc3c",
            "tdsql3-d8fffc4s"
        ],
        "FailedInstanceIds": [
            "tdsql3-d8fffc4s"
        ],
        "RequestId": "a93d2900-ef72-11eb-ab93-0716f253da76"
    }
}
```

