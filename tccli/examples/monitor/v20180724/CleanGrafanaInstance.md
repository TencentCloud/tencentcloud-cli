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
        "RequestId": "xxx"
    }
}
```

