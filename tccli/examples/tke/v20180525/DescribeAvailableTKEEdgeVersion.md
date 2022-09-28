**Example 1: 检查当前支持的k8s版本**



Input: 

```
tccli tke DescribeAvailableTKEEdgeVersion --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "Versions": [
            "1.14.1",
            "1.16.1"
        ],
        "EdgeVersionLatest": "1.0.1",
        "EdgeVersionCurrent": "1.0.1",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

