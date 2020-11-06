**Example 1: 解绑黑石负载均衡四层监听器物理服务器**



Input: 

```
tccli bmlb UnbindL4Backends --cli-unfold-argument  \
    --LoadBalancerId lb-dyxceyv5 \
    --ListenerId lbl-i4go349z \
    --BackendSet.0.Port 5001 \
    --BackendSet.0.InstanceId cpm-buj66q9x \
    --BindType 0
```

Output: 
```
{
    "Response": {
        "TaskId": 2385689,
        "RequestId": "c63625d4-5db2-403b-862a-19443923ed77"
    }
}
```

