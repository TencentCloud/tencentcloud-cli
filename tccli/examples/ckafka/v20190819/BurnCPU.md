**Example 1: CPU高负载**

CPU高负载

Input: 

```
tccli ckafka BurnCPU --cli-unfold-argument  \
    --InstanceId abc \
    --LoadRate 60 \
    --Duration 60
```

Output: 
```
{
    "Response": {
        "Code": 1,
        "Msg": "abc",
        "AsyncRequestId": "abc",
        "RequestId": "abc"
    }
}
```

