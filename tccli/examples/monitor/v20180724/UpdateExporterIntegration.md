**Example 1: 更新 exporter 集成配置**



Input: 

```
tccli monitor UpdateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --KubeType 3 \
    --ClusterId  \
    --Kind blackbox-exporter \
    --Content {"name":"test","kind":"blackbox-exporter","spec":{"instanceSpec":{"module":"http_get","urls":["xx"]}}}
```

Output: 
```
{
    "Response": {
        "RequestId": "wpkysykx8k9tu1urmlyo54gq33f4kxwz"
    }
}
```

