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
        "RequestId": "abc"
    }
}
```

