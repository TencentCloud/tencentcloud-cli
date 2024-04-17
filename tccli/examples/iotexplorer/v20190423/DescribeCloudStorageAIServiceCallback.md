**Example 1: 查询云存AI分析回调配置**



Input: 

```
tccli iotexplorer DescribeCloudStorageAIServiceCallback --cli-unfold-argument  \
    --ProductId KH6Q8C4N0D
```

Output: 
```
{
    "Response": {
        "Type": "http",
        "CallbackUrl": "https://yourdomain.com/api",
        "CallbackToken": "your-token",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

