**Example 1: 创建公网网络配置**

创建公网网络配置

Input: 

```
tccli tse CreateCloudNativeAPIGatewayPublicNetwork --cli-unfold-argument  \
    --GatewayId abc \
    --GroupId abc \
    --InternetConfig.InternetAddressVersion abc \
    --InternetConfig.InternetPayMode abc \
    --InternetConfig.InternetMaxBandwidthOut 1 \
    --InternetConfig.Description abc \
    --InternetConfig.SlaType abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

