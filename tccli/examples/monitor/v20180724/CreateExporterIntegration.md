**Example 1: 创建 blackbox-exporter 集成**



Input: 

```
tccli monitor CreateExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --Kind blackbox-exporter \
    --Content {"name":"test","kind":"blackbox-exporter","spec":{"instanceSpec":{"module":"http_get","urls":["http://abc"]}}}
```

Output: 
```
{
    "Response": {
        "Names": [
            "test"
        ],
        "RequestId": "xyz"
    }
}
```

