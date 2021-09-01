**Example 1: 绑定黑石物理服务器到四层监听器**



Input: 

```
tccli bmlb BindL4Backends --cli-unfold-argument  \
    --LoadBalancerId lb-dyxceyv5 \
    --ListenerId lbl-i4go349z \
    --BindType 0 \
    --BackendSet.0.Port 5000 \
    --BackendSet.0.InstanceId cpm-buj66q9x \
    --BackendSet.0.Weight 100
```

Output: 
```
{
    "Response": {
        "TaskId": "2385687",
        "RequestId": "eb162e39-cfeb-4de2-a7e3-495f9332fe28"
    }
}
```

