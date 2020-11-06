**Example 1: 设置流量镜像的健康检查参数**



Input: 

```
tccli bmlb SetTrafficMirrorHealthSwitch --cli-unfold-argument  \
    --TrafficMirrorId bmtm-lmep0eit \
    --HealthSwitch 1 \
    --HealthNum 2 \
    --UnhealthNum 3 \
    --IntervalTime 90 \
    --HttpCheckDomain a.com \
    --HttpCheckPath /a/a \
    --HttpCodes 1
```

Output: 
```
{
    "Response": {
        "TaskId": "123456LBTASKID",
        "RequestId": "9263d8ee-2a73-44fc-a7c2-81c6038ca263"
    }
}
```

