**Example 1: 创建服务来源实例**



Input: 

```
tccli tse CreateNativeGatewayServiceSource --cli-unfold-argument  \
    --GatewayID gateway-dde03567 \
    --SourceID ins-5ef8277d \
    --SourceName nacos-learn-prod \
    --SourceType TSE-Nacos \
    --SourceInfo.Addresses 10.0.0.1:8848 \
    --SourceInfo.VpcInfo.VpcID vpc-83p03121 \
    --SourceInfo.VpcInfo.SubnetID subnet-83p03121 \
    --SourceInfo.Auth.Username tse@tencentUser \
    --SourceInfo.Auth.Password tse@tencentPwd
```

Output: 
```
{
    "Response": {
        "Result": true,
        "SourceID": "cls-koqdd0fq",
        "RequestId": "0f1f5ecf-cf0d-47ea-95c4-7ebe260c2f06"
    }
}
```

