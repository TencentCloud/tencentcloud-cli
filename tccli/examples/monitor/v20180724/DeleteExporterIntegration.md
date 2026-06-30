**Example 1: DeleteExporterIntegration**



Input: 

```
tccli monitor DeleteExporterIntegration --cli-unfold-argument  \
    --InstanceId prom-1 \
    --KubeType 3 \
    --ClusterId cls-xx \
    --Kind mysql-exporter \
    --Name integration-name
```

Output: 
```
{
    "Response": {
        "RequestId": "xyz"
    }
}
```

