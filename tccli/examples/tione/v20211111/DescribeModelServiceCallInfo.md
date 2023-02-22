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
            "ServiceGroupId": "ms-p8w5zvh7",
            "InnerHttpAddr": "http://service-cmpdh0cg-1308945662-in.gz.apigw.tencentcs.com:8001/tione",
            "InnerHttpsAddr": "https://service-cmpdh0cg-1308945662-in.gz.apigw.tencentcs.com:9001/tione",
            "OuterHttpAddr": "http://service-cmpdh0cg-1308945662.gz.apigw.tencentcs.com:80/tione",
            "OuterHttpsAddr": "https://service-cmpdh0cg-1308945662.gz.apigw.tencentcs.com:443/tione",
            "AppKey": "",
            "AppSecret": ""
        },
        "InferGatewayCallInfo": {
            "VpcHttpAddr": "xx",
            "VpcHttpsAddr": "xx",
            "VpcGrpcTlsAddr": "xx",
            "VpcId": "xx",
            "SubnetId": "xx"
        },
        "DefaultNginxGatewayCallInfo": {
            "Host": "xx"
        },
        "RequestId": "8db93f56-6061-44ae-9e69-41ec47577db4"
    }
}
```

