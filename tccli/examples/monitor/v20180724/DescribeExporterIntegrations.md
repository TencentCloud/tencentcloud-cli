**Example 1: 查询 exporter 集成列表**

查询 exporter 集成列表

Input: 

```
tccli monitor DescribeExporterIntegrations --cli-unfold-argument  \
    --InstanceId prom-evrh1x32 \
    --Kind mysql-exporter \
    --ClusterId cls-evrh1x32 \
    --KubeType 3
```

Output: 
```
{
    "Response": {
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc",
        "IntegrationSet": []
    }
}
```

