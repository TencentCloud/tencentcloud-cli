**Example 1: Querying bandwidth package resources**



Input: 

```
tccli vpc DescribeBandwidthPackages --cli-unfold-argument  \
    --Filters.0.Name network-type\
    --Filters.0.Values BGP
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "BandwidthPackageSet": [
            {
                "BandwidthPackageId": "bwp-drmwgz9k",
                "NetworkType": "BGP",
                "ChargeType": "TOP5_POSTPAID_BY_MONTH",
                "BandwidthPackageName": "test",
                "CreatedTime": "2018-07-07T09:12:00Z",
                "Status": "CREATED",
                "ResourceSet": [
                    {
                        "ResourceType": "Address",
                        "ResourceId": "eip-53wbxk2o",
                        "AddressIp": "203.195.149.219"
                    }
                ]
            }
        ],
        "RequestId": "e886604e-6f02-4139-a596-8f959f8dfbe3"
    }
}
```

