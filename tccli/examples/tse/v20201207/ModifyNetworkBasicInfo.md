**Example 1: 修改网关实例网络基本信息**

修改Kong客户端内网网络信息

Input: 

```
tccli tse ModifyNetworkBasicInfo --cli-unfold-argument  \
    --GatewayId gatway-xxxxxx \
    --GroupId group-xxxxxx \
    --NetworkType Open \
    --Vip 172.10.10.1 \
    --InternetMaxBandwidthOut 1 \
    --Description test
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

