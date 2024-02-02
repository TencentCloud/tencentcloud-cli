**Example 1: 服务调用地址查询**

查询某个服务

Input: 

```
tccli tione DescribeModelServiceCallInfo --cli-unfold-argument  \
    --ServiceGroupId ms-p8w5zvh7
```

Output: 
```
{
    "Response": {
        "ServiceCallInfo": {
            "ServiceGroupId": "ms-ndxkhtb2",
            "InnerHttpAddr": "http://service-5a4oixv0-1256580188-in.gz.tencentapigw.com:8011/tione",
            "InnerHttpsAddr": "https://service-5a4oixv0-1256580188-in.gz.tencentapigw.com:9011/tione",
            "OuterHttpAddr": "http://service-5a4oixv0-1256580188.gz.tencentapigw.com:80/tione",
            "OuterHttpsAddr": "https://service-5a4oixv0-1256580188.gz.tencentapigw.com:443/tione",
            "AppKey": "APID23ycs7qbGGbTf27PG18oOVK1Q449UORNA1g5",
            "AppSecret": "bD2krm7a7ujt6779kLKV1g0x4n2z861IcguAMm6v",
            "AuthorizationEnable": true
        },
        "InferGatewayCallInfo": null,
        "DefaultNginxGatewayCallInfo": null,
        "TJCallInfo": null,
        "IntranetCallInfo": {
            "IngressPrivateLinkInfo": null,
            "ServiceEIPInfo": []
        },
        "RequestId": "0e26af99-dc12-4866-b6cf-1896a10c2910"
    }
}
```

