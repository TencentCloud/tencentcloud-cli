**Example 1: 创建 exporter 集成**



Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --KubeType 3 \
    --ClusterId cls-xx \
    --Kind blackbox-exporter \
    --Content {"name":"test","kind":"blackbox-exporter","spec":{"instanceSpec":{"module":"http_get","urls":["xx"]}}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "redis-exporter"
        ],
        "RequestId": "xyz"
    }
}
```

