**Example 1: 更新 Grafana 环境变量**

更新 Grafana 环境变量

Input: 

```
tccli monitor UpdateGrafanaEnvironments --cli-unfold-argument  \
    --InstanceId grafana-12345678 \
    --Envs {}
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

