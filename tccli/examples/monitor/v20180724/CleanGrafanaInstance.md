**Example 1: 强制销毁 Grafana 实例**

强制销毁 Grafana 实例

Input: 

```
tccli monitor CleanGrafanaInstance --cli-unfold-argument  \
    --InstanceId grafana-abcdefgh
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

