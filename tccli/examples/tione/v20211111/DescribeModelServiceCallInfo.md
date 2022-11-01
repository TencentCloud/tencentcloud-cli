**Example 1: 查询服务调用**



Input: 

```
tccli tione DescribeModelServiceCallInfo --cli-unfold-argument  \
    --ServiceGroupId ms-xxxx
```

Output: 
```
{
    "Response": {
        "ServiceCallInfo": {
            "ServiceGroupId": "ms-xxxxx",
            "InnerHttpAddr": "http://service-xxxxx-00000-in.gz.apigw.tencentcs.com:8009/tione",
            "InnerHttpsAddr": "https://service-xxxxx-000000-in.gz.apigw.tencentcs.com:9009/tione",
            "OuterHttpAddr": "http://service-xxxx-00000.gz.apigw.tencentcs.com:80/tione",
            "OuterHttpsAddr": "https://service-xxxx-00000.gz.apigw.tencentcs.com:443/tione",
            "AppKey": "",
            "AppSecret": ""
        },
        "InferGatewayCallInfo": {
            "SubnetId": "xx",
            "VpcHttpsAddr": "xx",
            "VpcHttpAddr": "xx",
            "VpcId": "xx",
            "VpcGrpcTlsAddr": "xx"
        },
        "RequestId": "5203eb3a-366e-4e14-bd59-afe109849377"
    }
}
```

