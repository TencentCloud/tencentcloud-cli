**Example 1: 创建云原生API网关实例**

创建云原生API网关实例

Input: 

```
tccli tse CreateCloudNativeAPIGateway --cli-unfold-argument  \
    --Name test \
    --Type kong \
    --GatewayVersion 2.5.1 \
    --NodeConfig.Specification 1c2g \
    --NodeConfig.Number 2 \
    --VpcConfig.VpcId vpc-xxxxxx \
    --VpcConfig.SubnetId subnet-xxxxxx \
    --Description test \
    --Tags.0.TagKey abc \
    --Tags.0.TagValue abc \
    --EnableCls False \
    --FeatureVersion STANDARD \
    --InternetMaxBandwidthOut 1 \
    --EngineRegion ap-guangzhou \
    --IngressClassName abc \
    --TradeType 0 \
    --InternetConfig.InternetAddressVersion abc \
    --InternetConfig.InternetPayMode abc \
    --InternetConfig.InternetMaxBandwidthOut 1 \
    --InternetConfig.Description abc \
    --InternetConfig.SlaType abc \
    --InternetConfig.MultiZoneFlag True \
    --InternetConfig.MasterZoneId abc \
    --InternetConfig.SlaveZoneId abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "GatewayId": "abc",
            "Status": "abc",
            "TaskId": "abc"
        },
        "RequestId": "abc"
    }
}
```

