**Example 1: nat所在地域防火墙集群部署状态**

nat所在地域防火墙集群部署状态

Input: 

```
tccli cfw DescribeNatFwClusterRegionStatus --cli-unfold-argument  \
    --NatClusterRegionStatusQueryList.0.CcnId ccn-c0qmm031 \
    --NatClusterRegionStatusQueryList.0.NatInsId nat-45yn1tks \
    --NatClusterRegionStatusQueryList.0.AssetType nat_ccn \
    --NatClusterRegionStatusQueryList.0.RoutingMode 1
```

Output: 
```
{
    "Response": {
        "RegionFwStatus": [
            {
                "CcnId": "ccn-c0qmm031",
                "Cidr": "10.31.0.0/26",
                "NatInsId": "nat-45yn1tks",
                "Region": "eu-frankfurt",
                "RoutingMode": 1,
                "Status": "Custom"
            }
        ],
        "Total": 1,
        "RequestId": "fd6c0cc2-0be1-437e-b363-de4384c2c2da"
    }
}
```

