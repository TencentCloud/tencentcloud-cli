**Example 1: 创建云交换服务通道**

创建云交换服务通道

Input: 

```
tccli dc CreateDirectConnectTunnel --cli-unfold-argument  \
    --DirectConnectId dc-juystu9z \
    --DirectConnectTunnelName testvif \
    --NetworkType CCN \
    --NetworkRegion ap-guangzhou \
    --DirectConnectGatewayId dcg-du8uzrih \
    --Bandwidth 100 \
    --RouteType BGP \
    --Vlan 1001
```

Output: 
```
{
    "Response": {
        "DirectConnectTunnelIdSet": [
            "dcx-inx9ty4u"
        ],
        "RequestId": "4539586b-d0d7-49bb-b351-2036da9ac277"
    }
}
```

**Example 2: BGP路由模式和云联网专用通道**

BGP路由模式和云联网专用通道

Input: 

```
tccli dc CreateDirectConnectTunnel --cli-unfold-argument  \
    --DirectConnectId dc-abcdefgh \
    --DirectConnectTunnelName Test \
    --NetworkType CCN \
    --NetworkRegion ap-guangzhou \
    --DirectConnectGatewayId dcg-abcdefgh \
    --Bandwidth 100 \
    --RouteType BGP \
    --Vlan 100 \
    --TencentAddress 192.168.1.2/30 \
    --CustomerAddress 192.168.1.1/30 \
    --BgpPeer.Asn 65128 \
    --BgpPeer.AuthKey abcdefg
```

Output: 
```
{
    "Response": {
        "DirectConnectTunnelIdSet": [
            "dcx-abcdefgh"
        ],
        "RequestId": "24a0d7e5-4c13-49be-aa16-94f698fbef3e"
    }
}
```

**Example 3: BGP路由模式和共享专线的专用通道**

BGP路由模式和共享专线的专用通道

Input: 

```
tccli dc CreateDirectConnectTunnel --cli-unfold-argument  \
    --DirectConnectId dc-abcdefgh \
    --DirectConnectTunnelName Test \
    --DirectConnectOwnerAccount 240791248 \
    --NetworkType VPC \
    --NetworkRegion ap-guangzhou \
    --VpcId vpc-abcdefgh \
    --DirectConnectGatewayId dcg-abcdefgh \
    --Bandwidth 100 \
    --RouteType BGP \
    --Vlan 100 \
    --TencentAddress 192.168.1.2/30 \
    --CustomerAddress 192.168.1.1/30 \
    --BgpPeer.Asn 65128 \
    --BgpPeer.AuthKey abcdefg
```

Output: 
```
{
    "Response": {
        "DirectConnectTunnelIdSet": [
            "dcx-abcdefgh"
        ],
        "RequestId": "24a0d7e5-4c13-49be-aa16-94f698fbef3e"
    }
}
```

**Example 4: STATIC路由模式和黑石VPC的专用通道**

STATIC路由模式和黑石VPC的专用通道

Input: 

```
tccli dc CreateDirectConnectTunnel --cli-unfold-argument  \
    --DirectConnectId dc-abcdefgh \
    --DirectConnectTunnelName Test \
    --NetworkType BMVPC \
    --NetworkRegion ap-guangzhou \
    --VpcId vpc-abcdefgh \
    --Bandwidth 100 \
    --RouteType STATIC \
    --Vlan 100 \
    --TencentAddress 192.168.1.2/30 \
    --CustomerAddress 192.168.1.1/30 \
    --RouteFilterPrefixes.0.Cidr 192.168.0.0/24 \
    --RouteFilterPrefixes.1.Cidr 192.168.0.0/24 \
    --RouteFilterPrefixes.2.Cidr 192.168.0.0/24
```

Output: 
```
{
    "Response": {
        "DirectConnectTunnelIdSet": [
            "dcx-abcdefgh"
        ],
        "RequestId": "24a0d7e5-4c13-49be-aa16-94f698fbef3e"
    }
}
```

**Example 5: BGP路由模式和私有网络VPC的专用通道**

BGP路由模式和私有网络VPC的专用通道

Input: 

```
tccli dc CreateDirectConnectTunnel --cli-unfold-argument  \
    --DirectConnectId dc-abcdefgh \
    --DirectConnectTunnelName Test \
    --NetworkType VPC \
    --NetworkRegion ap-guangzhou \
    --VpcId vpc-abcdefgh \
    --DirectConnectGatewayId dcg-abcdefgh \
    --Bandwidth 100 \
    --RouteType BGP \
    --Vlan 100 \
    --TencentAddress 192.168.1.2/30 \
    --CustomerAddress 192.168.1.1/30 \
    --BgpPeer.Asn 65128 \
    --BgpPeer.AuthKey abcdefg
```

Output: 
```
{
    "Response": {
        "DirectConnectTunnelIdSet": [
            "dcx-abcdefgh"
        ],
        "RequestId": "24a0d7e5-4c13-49be-aa16-94f698fbef3e"
    }
}
```

