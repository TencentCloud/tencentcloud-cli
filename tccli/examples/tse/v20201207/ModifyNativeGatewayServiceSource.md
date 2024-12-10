**Example 1: ModifyNativeGatewayServiceSource**



Input: 

```
tccli tse ModifyNativeGatewayServiceSource --cli-unfold-argument  \
    --GatewayID gateway-dde03567 \
    --SourceID ins-5ef8277d \
    --SourceName nacos-learn-prod \
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
        "RequestId": "0f1f5ecf-cf0d-47ea-95c4-7ebe260c2f06"
    }
}
```

