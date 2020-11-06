**Example 1: 绑定黑石物理服务器成为流量镜像接收机**



Input: 

```
tccli bmlb BindTrafficMirrorReceivers --cli-unfold-argument  \
    --TrafficMirrorId bmtm-lmep0eit \
    --ReceiverSet.0.Port 113 \
    --ReceiverSet.0.InstanceId tcpm-px13l9jh \
    --ReceiverSet.0.Weight 100
```

Output: 
```
{
    "Response": {
        "TaskId": "123456LBTASKID",
        "RequestId": "3697fa73-c8c0-4471-9966-749f62a0fadb"
    }
}
```

