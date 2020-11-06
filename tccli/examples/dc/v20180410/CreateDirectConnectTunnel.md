**Example 1: Dedicated tunnel using BGP routing and shared connection**



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

**Example 2: Dedicated tunnel using BGP routing and CCN**



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

**Example 3: Dedicated tunnel using static routing and BM VPC**



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

**Example 4: Dedicated tunnel using BGP routing and VPC**



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

