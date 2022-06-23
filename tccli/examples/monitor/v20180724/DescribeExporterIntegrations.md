**Example 1: 查询 exporter 集成列表**



Input: 

```
tccli monitor DescribeExporterIntegrations --cli-unfold-argument  \
    --InstanceId xx \
    --Kind xx \
    --ClusterId xx \
    --KubeType 3
```

Output: 
```
{
    "Response": {
        "RequestId": "wpkysykx8k9tu1urmlyo54gq33f4kxwz",
        "IntegrationSet": []
    }
}
```

