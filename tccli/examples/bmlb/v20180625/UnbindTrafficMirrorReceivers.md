**Example 1: 从流量镜像实例上解绑流量镜像接收机**



Input: 

```
tccli bmlb UnbindTrafficMirrorReceivers --cli-unfold-argument  \
    --TrafficMirrorId bmtm-lmep0eit \
    --ReceiverSet.0.Port 113 \
    --ReceiverSet.0.InstanceId tcpm-px13l9jh
```

Output: 
```
{
    "Response": {
        "TaskId": "123456LBTASKID",
        "RequestId": "cd16d728-1694-46a3-a927-9216599c0dd7"
    }
}
```

