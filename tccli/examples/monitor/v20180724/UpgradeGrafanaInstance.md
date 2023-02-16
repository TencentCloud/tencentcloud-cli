**Example 1: 升级 Grafana 实例**

升级 Grafana 实例

Input: 

```
tccli monitor UpgradeGrafanaInstance --cli-unfold-argument  \
    --InstanceId grafana-12345678 \
    --Alias v7.4.2
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

