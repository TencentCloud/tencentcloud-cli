**Example 1: 查询SSL-VPN-CLIENT**

查询SSL-VPN-CLIENT

Input: 

```
tccli vpc DescribeVpnGatewaySslClients --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2 \
    --Filters.0.Name vpn-gateway-id \
    --Filters.0.Values vpn-123456
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SslVpnClientSet": [
            {
                "VpcId": "vpc-ez3k7doq",
                "SslVpnServerId": "vpns-80pwpme0",
                "CertStatus": 1,
                "SslVpnClientId": "vpnc-dyc72w04",
                "CertBeginTime": "2021-11-15 19:48:20",
                "CertEndTime": "2024-11-14 19:48:20",
                "Name": "SSL-VPN-CLIENT",
                "State": "6"
            }
        ],
        "RequestId": "fe40c051-723d-4cf7-9838-71d5684f2cbb"
    }
}
```

