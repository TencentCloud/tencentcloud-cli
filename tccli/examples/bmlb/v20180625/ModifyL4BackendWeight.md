**Example 1: 修改黑石负载均衡四层监听器后端实例权重**



Input: 

```
tccli bmlb ModifyL4BackendWeight --cli-unfold-argument  \
    --LoadBalancerId lb-dyxceyv5 \
    --ListenerId lbl-i4go349z \
    --InstanceId cpm-buj66q9x \
    --Port 5001 \
    --BindType 0 \
    --Weight 99
```

Output: 
```
{
    "Response": {
        "TaskId": "2385687LBTASKID",
        "RequestId": "e7aa7e32-ffa9-47fb-8416-4fafda91ca6b"
    }
}
```

