**Example 1: 关机**

关机

Input: 

```
tccli ckafka InjectDownAttack --cli-unfold-argument  \
    --InstanceId abc \
    --InjectZoneId 1
```

Output: 
```
{
    "Response": {
        "Code": 1,
        "AsyncRequestId": "abc",
        "Msg": "abc",
        "RequestId": "1305a410-b030-476d-acdf-eba0dfd5323b"
    }
}
```

