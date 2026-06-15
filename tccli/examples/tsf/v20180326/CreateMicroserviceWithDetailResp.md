**Example 1: 新增微服务返回ID**



Input: 

```
tccli tsf CreateMicroserviceWithDetailResp --cli-unfold-argument  \
    --NamespaceId namespace-9ynm2mea \
    --MicroserviceName provider-demo-mock \
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
        "Result": "ms-alb4jggv",
        "RequestId": "8bb8485c-977c-4fa9-aa7d-b6c000f44d8d"
    }
}
```

