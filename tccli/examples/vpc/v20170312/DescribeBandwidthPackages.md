**Example 1: 查询带宽包资源**



Input: 

```
tccli vpc DescribeBandwidthPackages --cli-unfold-argument  \
    --Filters.0.Values BGP \
    --Filters.0.Name network-type
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "BandwidthPackageSet": [
            {
                "BandwidthPackageId": "bwp-p6am50q0",
                "BandwidthPackageName": "gongxiang1",
                "Status": "CREATED",
                "NetworkType": "BGP",
                "ChargeType": "FIXED_PREPAID_BY_MONTH",
                "CreatedTime": "2019-12-31T16:48:49Z",
                "ResourceSet": [
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-hbhcbwci",
                        "AddressIp": "134.175.210.185"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-bksqvcue",
                        "AddressIp": "193.112.158.4"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-rlwrl9zg",
                        "AddressIp": "193.112.128.149"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-0a0z6e86",
                        "AddressIp": "193.112.214.231"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-loq78a2u",
                        "AddressIp": "193.112.214.146"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-9b23ko6g",
                        "AddressIp": "193.112.195.106"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-l3utrirm",
                        "AddressIp": "193.112.214.252"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-biawxrrg",
                        "AddressIp": "193.112.161.62"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-gm8dcbmw",
                        "AddressIp": "129.204.145.2"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-f3yjemhw",
                        "AddressIp": "134.175.169.60"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-oahxub36",
                        "AddressIp": "106.53.87.77"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-ej9oasck",
                        "AddressIp": "193.112.186.94"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-iivgnxr6",
                        "AddressIp": "106.52.155.79"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-9pva2ne6",
                        "AddressIp": "106.52.167.45"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-fqexkiku",
                        "AddressIp": "129.204.251.201"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-dorh1ejy",
                        "AddressIp": "106.55.92.150"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-pdxzxuzs",
                        "AddressIp": "42.194.204.43"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-26tl14zo",
                        "AddressIp": "106.52.248.58"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-1n624fs0",
                        "AddressIp": "106.55.63.197"
                    },
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-j4s0mcug",
                        "AddressIp": "106.55.92.154"
                    }
                ],
                "Bandwidth": 500
            }
        ],
        "RequestId": "e0ee5afd-a684-4a4c-9fff-ef5d626aed46"
    }
}
```

