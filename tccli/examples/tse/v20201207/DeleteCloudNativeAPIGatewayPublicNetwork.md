**Example 1: 删除网关实例公网网络**

删除网关实例客户端公网网络

Input: 

```
tccli tse DeleteCloudNativeAPIGatewayPublicNetwork --cli-unfold-argument  \
    --GatewayId abc \
    --GroupId abc \
    --InternetAddressVersion abc \
    --Vip abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

