**Example 1: 创建 IDC 通道**

创建 IDC 通道

Input: 

```
tccli vpc CreateCdcLDCXList --cli-unfold-argument  \
    --CdcLDCXSet.0.CdcId cluster-d8htgb6k \
    --CdcLDCXSet.0.NetPlaneId np-b6ebdd49 \
    --CdcLDCXSet.0.Name ivan_namt \
    --CdcLDCXSet.0.Description ivan_description \
    --CdcLDCXSet.0.ConnType VRRP \
    --CdcLDCXSet.0.RouteType BGP \
    --CdcLDCXSet.0.VlanId 3001 \
    --CdcLDCXSet.0.ConnIpInfoSet.0.LocalIp 1.1.1.1 \
    --CdcLDCXSet.0.ConnIpInfoSet.0.PeerIp 1.1.1.10 \
    --CdcLDCXSet.0.ConnIpInfoSet.0.IntMask 25 \
    --CdcLDCXSet.0.ConnIpInfoSet.1.LocalIp 1.1.1.2 \
    --CdcLDCXSet.0.ConnIpInfoSet.1.PeerIp 1.1.1.10 \
    --CdcLDCXSet.0.ConnIpInfoSet.1.IntMask 25 \
    --CdcLDCXSet.0.BgpInfo.BgpAsn 100 \
    --CdcLDCXSet.0.BgpInfo.BgpKey 123456 \
    --CdcLDCXSet.0.IdcCidrSet 10.0.0.0/24 172.16.0.0/24 \
    --CdcLDCXSet.0.VRRP.Id 200 \
    --CdcLDCXSet.0.VRRP.Vip 1.1.1.3 \
    --CdcLDCXSet.0.ModeDetect.DetectMode BFD \
    --CdcLDCXSet.0.ModeDetect.DetectMultiplier 20 \
    --CdcLDCXSet.0.ModeDetect.DetectInterval 5000
```

Output: 
```
{
    "Response": {
        "CdcLDCXSet": [
            {
                "BgpInfo": {
                    "BgpAsn": 100,
                    "BgpKey": "123456"
                },
                "CdcId": "cluster-d8htgb6k",
                "ConnIpInfoSet": [
                    {
                        "IntMask": 25,
                        "LocalIp": "1.1.1.1",
                        "PeerIp": "1.1.1.10"
                    },
                    {
                        "IntMask": 25,
                        "LocalIp": "1.1.1.2",
                        "PeerIp": "1.1.1.10"
                    }
                ],
                "ConnType": "VRRP",
                "CreateTime": "2024-01-19T14:08:20.727174",
                "Description": "ivan_description",
                "IdcCidrSet": [
                    ""
                ],
                "LDCXId": "ldcx-b179f998",
                "ModeDetect": {
                    "DetectInterval": 5000,
                    "DetectMode": "BFD",
                    "DetectMultiplier": 20
                },
                "Name": "ivan_namt",
                "NetPlaneId": "np-b6ebdd49",
                "RouteType": "BGP",
                "UpdateTime": "2024-01-19T14:08:20.727187",
                "VRRP": {
                    "Id": 200,
                    "Vip": "1.1.1.3"
                },
                "VlanId": 3001
            }
        ],
        "RequestId": "cf9c4a26-aaa5-4271-91e6-2351bfaddd17",
        "TotalCount": 1
    }
}
```

