**Example 1: 查询指定产品的云存 AI 服务开通状态**



Input: 

```
tccli iotexplorer DescribeProductCloudStorageAIService --cli-unfold-argument  \
    --ProductId KH6Q8C4N0D
```

Output: 
```
{
    "Response": {
        "Enabled": true,
        "Available": true,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

