**Example 1: 修改路由模式是BGP的专用通道**



Input: 

```
tccli dc ModifyDirectConnectTunnelAttribute --cli-unfold-argument  \
    --DirectConnectTunnelId dcx-abcdefgh \
    --DirectConnectTunnelName Test \
    --Bandwidth 100 \
    --TencentAddress 192.168.1.1/30 \
    --CustomerAddress 192.168.1.2/30 \
    --BgpPeer.Asn 65128 \
    --BgpPeer.AuthKey abcdefg
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 修改路由模式是STATIC的专用通道**



Input: 

```
tccli dc ModifyDirectConnectTunnelAttribute --cli-unfold-argument  \
    --DirectConnectTunnelId dcx-abcdefgh \
    --DirectConnectTunnelName Test \
    --Bandwidth 100 \
    --TencentAddress 192.168.1.1/30 \
    --CustomerAddress 192.168.1.2/30 \
    --RouteFilterPrefixes.0.Cidr 192.168.0.0/24 \
    --RouteFilterPrefixes.1.Cidr 192.168.1.0/24 \
    --RouteFilterPrefixes.2.Cidr 192.168.2.0/24
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

