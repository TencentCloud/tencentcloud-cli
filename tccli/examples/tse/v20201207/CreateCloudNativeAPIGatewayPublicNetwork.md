**Example 1: 创建公网网络配置**

创建公网网络配置

Input: 

```
tccli tse CreateCloudNativeAPIGatewayPublicNetwork --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --GroupId group-4se0czf7 \
    --InternetConfig.InternetAddressVersion IPV4 \
    --InternetConfig.InternetPayMode TRAFFIC \
    --InternetConfig.InternetMaxBandwidthOut 1 \
    --InternetConfig.Description 公网负载均衡 \
    --InternetConfig.SlaType clb.c4.small
```

Output: 
```
{
    "Response": {
        "RequestId": "a02f30b2-6e3d-4efb-9883-1b11b8fa7df2"
    }
}
```

