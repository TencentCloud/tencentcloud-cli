**Example 1: 查询 IDC通道配置**



Input: 

```
tccli vpc DescribeCdcLDCXList --cli-unfold-argument  \
    --Filters.0.Name net-plane-id \
    --Filters.0.Values np-efe0238e
```

Output: 
```
{
    "Response": {
        "CdcLDCXSet": [
            {
                "NetPlaneId": "np-efe0238e",
                "CdcId": "cluster-d8htgb6k",
                "Name": "demo",
                "Description": "demo",
                "ConnType": "VRRP",
                "RouteType": "BGP",
                "VlanId": 3100,
                "CreateTime": "2024-01-11T11:39:53.582775",
                "UpdateTime": "2024-01-11T13:59:28.022514",
                "BgpInfo": {
                    "BgpAsn": 100,
                    "BgpKey": "bgpkey"
                },
                "ModeDetect": {
                    "DetectMode": "BFD",
                    "DetectMultiplier": 20,
                    "DetectInterval": 5000
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "091e2a8d-8ce0-4e98-994b-79ebb093316b"
    }
}
```

