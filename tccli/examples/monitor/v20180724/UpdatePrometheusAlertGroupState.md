**Example 1: 设置告警分组禁用**

设置告警分组禁用

Input: 

```
tccli monitor UpdatePrometheusAlertGroupState --cli-unfold-argument  \
    --InstanceId prom-7vp71mk0 \
    --GroupIds alert-ol72w8vy \
    --GroupState 3
```

Output: 
```
{
    "Response": {
        "RequestId": "a4797141-a4f9-43d4-b4ca-09d72bb48f8d"
    }
}
```

