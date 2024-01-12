**Example 1: 删除告警分组**

删除告警分组

Input: 

```
tccli monitor DeletePrometheusAlertGroups --cli-unfold-argument  \
    --InstanceId prom-7vp71mk0 \
    --GroupIds alert-ol72w8vy
```

Output: 
```
{
    "Response": {
        "RequestId": "09cffdc9-047e-45c5-b0eb-6d7cbfee5048"
    }
}
```

