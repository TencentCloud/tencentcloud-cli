**Example 1: 修改云原生API网关实例Konga网络配置**

修改云原生API网关实例Konga网络配置

Input: 

```
tccli tse ModifyConsoleNetwork --cli-unfold-argument  \
    --GatewayId gateway-xxxxxxxx \
    --NetworkType Open \
    --Operate Open
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

