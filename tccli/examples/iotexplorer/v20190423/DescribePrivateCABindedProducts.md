**Example 1: 请求示例**



Input: 

```
tccli iotexplorer DescribePrivateCABindedProducts --cli-unfold-argument  \
    --CertName smoke-not-exist \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Products": [],
        "RequestId": "302cf46d-c4d3-4ae4-bb9f-201f7a364566"
    }
}
```

