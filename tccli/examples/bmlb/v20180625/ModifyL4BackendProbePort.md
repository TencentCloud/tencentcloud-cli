**Example 1: 修改黑石负载均衡四层监听器后端探测端口**



Input: 

```
tccli bmlb ModifyL4BackendProbePort --cli-unfold-argument  \
    --LoadBalancerId lb-47gazeml \
    --ListenerId lbl-20tn33dz \
    --InstanceId tcpm-px13l9jh \
    --Port 333 \
    --ProbePort 666 \
    --BindType 0
```

Output: 
```
{
    "Response": {
        "TaskId": 2385730,
        "RequestId": "3683a122-ace5-46e2-b13b-90bfc4b5bae7"
    }
}
```

