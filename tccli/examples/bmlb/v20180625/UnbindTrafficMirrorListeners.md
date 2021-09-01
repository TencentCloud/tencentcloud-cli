**Example 1: 解绑流量镜像监听器**



Input: 

```
tccli bmlb UnbindTrafficMirrorListeners --cli-unfold-argument  \
    --TrafficMirrorId bmtm-lmep0eit \
    --ListenerIds lbl-3b8kycav
```

Output: 
```
{
    "Response": {
        "TaskId": "123456LBTASKID",
        "RequestId": "9965652f-df3e-469a-8fb6-11838bdf2c14"
    }
}
```

