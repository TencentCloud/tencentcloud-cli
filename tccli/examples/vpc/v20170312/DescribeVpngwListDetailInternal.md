**Example 1: demo**



Input: 

```
tccli vpc DescribeVpngwListDetailInternal --cli-unfold-argument  \
    --Owner 251197522 \
    --Limit 1 \
    --ImageId img2021011305837244
```

Output: 
```
{
    "Response": {
        "Total": 2,
        "GetVpngwListDetailResult": [
            {
                "VpcId": 81292,
                "UniqueVpcId": "vpc-7f2w7dl7",
                "HotHaMac": "50:54:A9:FE:80:07",
                "VpcDefaultFlag": 0,
                "InternalHotHaMask": "",
                "ImageId": "img2021011305837244",
                "HotHaMask": "255.255.128.0",
                "Bandwidth": 5,
                "VpcName": "new_test",
                "Owner": "251197522",
                "VpnConnectNum": 0,
                "MaxConnection": 5,
                "Zone": "ap-guangzhou-2",
                "UniqueCdcId": "",
                "VpcIntMask": 16,
                "VpcMask": "255.255.0.0",
                "ZoneId": 100002,
                "VpngwDomainIpPoolNum": 0,
                "State": 3,
                "WanIp": "",
                "InternalHotHaSubnet": "",
                "VpnType": 0,
                "AutoRenewalsFlag": 1,
                "VpcSubnet": "10.0.0.0",
                "Quota": "qc_mini",
                "DealId": "20210323292000292232301",
                "ExpireTime": "0000-00-00 00:00:00",
                "InternalHotHaMac": "",
                "VpngwDomainRtNum": 0,
                "VpngwId": 12201,
                "UniqVpngwId": "vpngw-eavy145z",
                "HotHaSubnet": "169.254.128.0",
                "CreateTime": "2021-03-23 16:01:01",
                "VpngwDomainNum": 0,
                "InternalHotHaIp": "",
                "SlaLocalIp": "0.0.0.0",
                "Name": "new_t_vpn_gw",
                "NewAfcFlag": 0,
                "HotHaFlag": 1,
                "VpngwDomainAclNum": 0,
                "HotHaIp": "169.254.128.7",
                "SSLVpnPort": 443,
                "BlockedFlag": 0
            }
        ],
        "RequestId": "0f6d3987-1b1d-4607-9782-614d03b63275"
    }
}
```

