**Example 1: ShowNatFwVpcDnsLst 展示租户NAT防火墙实例的vpc dns 开关信息**



Input: 

```
tccli cfw DescribeNatFwVpcDnsLst --cli-unfold-argument  \
    --NatFwInsId cfwnat-d1580b7b \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "VpcDnsSwitchLst": [
            {
                "SwitchStatus": 0,
                "NatInsId": "cfwnat-f3250045",
                "DNSEip": "121.5.27.250",
                "VpcIpv4Cidr": "10.115.0.0/16",
                "FwMode": 1,
                "VpcName": "wy",
                "VpcId": "vpc-ilbrv877"
            }
        ],
        "Total": 1,
        "ReturnMsg": "success",
        "RequestId": "50e39f16-3b3a-4c66-b76e-1705449ba828"
    }
}
```

