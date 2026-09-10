**Example 1: 创建内部北极星服务来源**

创建内部北极星服务来源

Input: 

```
tccli cngw CreateCloudNativeAPIGatewayAIServiceSource --cli-unfold-argument  \
    --GatewayId gateway-4e588095 \
    --SourceName 默认接入点 \
    --SourceType Registry \
    --SourceProduct InnerPolaris \
    --Description 默认接入点
```

Output: 
```
{
    "Response": {
        "Result": {
            "ID": "source-18fe1a4d31f51d6014ac",
            "Success": true
        },
        "RequestId": "f8b5d177-d4c7-4fbd-8318-fbfdb2880cb3"
    }
}
```

