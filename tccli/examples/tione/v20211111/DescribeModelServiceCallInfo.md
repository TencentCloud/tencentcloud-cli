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
            "ServiceGroupId": "abc",
            "InnerHttpAddr": "abc",
            "InnerHttpsAddr": "abc",
            "OuterHttpAddr": "abc",
            "OuterHttpsAddr": "abc",
            "AppKey": "abc",
            "AppSecret": "abc"
        },
        "InferGatewayCallInfo": {
            "VpcHttpAddr": "abc",
            "VpcHttpsAddr": "abc",
            "VpcGrpcTlsAddr": "abc",
            "VpcId": "abc",
            "SubnetId": "abc"
        },
        "DefaultNginxGatewayCallInfo": {
            "Host": "abc"
        },
        "TJCallInfo": {
            "HttpAddr": "abc",
            "Token": "abc",
            "CallExample": "abc"
        },
        "RequestId": "abc"
    }
}
```

