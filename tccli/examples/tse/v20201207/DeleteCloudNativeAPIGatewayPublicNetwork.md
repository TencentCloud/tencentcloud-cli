**Example 1: 删除网关实例公网网络**

删除网关实例客户端公网网络

Input: 

```
tccli tse DeleteCloudNativeAPIGatewayPublicNetwork --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --GroupId group-09ex5ff1 \
    --InternetAddressVersion IPV4 \
    --Vip 8.8.8.8
```

Output: 
```
{
    "Response": {
        "RequestId": "7a3a49de-660e-4b4c-aaec-05ddc2c31f48"
    }
}
```

