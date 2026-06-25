**Example 1: 创建微服务示例**



Input: 

```
tccli tsf CreateMicroservice --cli-unfold-argument  \
    --NamespaceId namespace-9ynm2mea \
    --MicroserviceName app-jolyonzheng \
    --MicroserviceDesc this is desc \
    --ServiceType SDK \
    --ServiceUrl www.tsf.com \
    --Protocol http \
    --ServiceDiscovery DNS
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "41521ae0-bce6-4bbe-af2a-753f7bb177ed"
    }
}
```

