**Example 1: 磁盘IO高负载**

磁盘IO高负载

Input: 

```
tccli ckafka BurnDiskIO --cli-unfold-argument  \
    --InstanceId abc \
    --Duration 60
```

Output: 
```
{
    "Response": {
        "Code": 1,
        "Msg": "abc",
        "AsyncRequestId": "abc",
        "RequestId": "1305a410-b030-476d-acdf-eba0dfd5323b"
    }
}
```

