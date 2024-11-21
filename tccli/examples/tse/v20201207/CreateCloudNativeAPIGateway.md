**Example 1: 创建云原生API网关实例**

创建云原生API网关实例

Input: 

```
tccli tse CreateCloudNativeAPIGateway --cli-unfold-argument  \
    --Name gateway-prod \
    --Type kong \
    --GatewayVersion 2.5.1 \
    --NodeConfig.Specification 1c2g \
    --NodeConfig.Number 2 \
    --VpcConfig.VpcId vpc-59cag821 \
    --VpcConfig.SubnetId subnet-8tzp8uz1 \
    --Description 公网入口网关，现网环境 \
    --Tags.0.TagKey env \
    --Tags.0.TagValue prod \
    --EnableCls False \
    --FeatureVersion STANDARD \
    --InternetMaxBandwidthOut 1 \
    --EngineRegion ap-guangzhou \
    --IngressClassName kong \
    --TradeType 0 \
    --InternetConfig.InternetAddressVersion IPV4 \
    --InternetConfig.InternetPayMode TRAFFIC \
    --InternetConfig.InternetMaxBandwidthOut 1 \
    --InternetConfig.Description 公网负载均衡 \
    --InternetConfig.SlaType clb.c2.medium \
    --InternetConfig.MultiZoneFlag True \
    --InternetConfig.MasterZoneId ap-guangzhou-3 \
    --InternetConfig.SlaveZoneId ap-guangzhou-4
```

Output: 
```
{
    "Response": {
        "Result": {
            "GatewayId": "gateway-dde03755",
            "Status": "Creating",
            "TaskId": "task-b2c41103"
        },
        "RequestId": "a02f30b2-6e3d-4efb-9883-1b11b8fa7df2"
    }
}
```

