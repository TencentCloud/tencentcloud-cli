**Example 1: 修改网关实例网络基本信息**

修改Kong客户端内网网络信息

Input: 

```
tccli tse ModifyNetworkBasicInfo --cli-unfold-argument  \
    --GatewayId gatway-dde03767 \
    --GroupId group-4se0czf7 \
    --NetworkType Open \
    --Vip 172.10.10.1 \
    --InternetMaxBandwidthOut 1 \
    --Description 公网入口负载均衡
```

Output: 
```
{
    "Response": {
        "RequestId": "ffadafb6-545d-461c-ad8c-baa26c0f8955"
    }
}
```

