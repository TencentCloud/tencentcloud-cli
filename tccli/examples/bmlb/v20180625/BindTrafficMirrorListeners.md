**Example 1: 绑定黑石服务器7层监听器到流量镜像实例**



Input: 

```
tccli bmlb BindTrafficMirrorListeners --cli-unfold-argument  \
    --TrafficMirrorId bmtm-lmep0eit \
    --ListenerIds lbl-3b8kycav
```

Output: 
```
{
    "Response": {
        "TaskId": "123456LBTASKID",
        "RequestId": "6f11420c-3bfe-4783-a928-07fe2653730f"
    }
}
```

