**Example 1: 获取一对VPN通道健康检查地址**

获取一对VPN通道健康检查地址

Input: 

```
tccli vpc GenerateVpnConnectionDefaultHealthCheckIp --cli-unfold-argument  \
    --VpnGatewayId vpn-ngenl4az
```

Output: 
```
{
    "Response": {
        "HealthCheckLocalIp": "169.254.128.2",
        "HealthCheckRemoteIp": "169.254.128.5",
        "RequestId": "6e446c86-d8c9-4981-9b33-d10956585058"
    }
}
```

