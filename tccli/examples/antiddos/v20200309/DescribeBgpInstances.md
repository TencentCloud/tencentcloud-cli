**Example 1: 后付费**



Input: 

```
tccli antiddos DescribeBgpInstances --cli-unfold-argument  \
    --FilterRegion ap-guangzhou \
    --FilterInstanceIdList bgp-000004rq \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "BGPInstanceList": [
            {
                "DryRun": false,
                "EnterprisePackageConfig": null,
                "InstanceChargePrepaid": {
                    "Period": 3,
                    "RenewFlag": null
                },
                "InstanceChargeType": "POSTPAID_BY_MONTH",
                "InstanceCount": 1,
                "InstanceId": "bgp-000004rq",
                "PackageType": "Standard",
                "StandardPackageConfig": {
                    "Bandwidth": 50,
                    "ElasticBandwidthFlag": false,
                    "ProtectIpCount": 10,
                    "Region": "ap-guangzhou"
                },
                "StandardPlusPackageConfig": null,
                "TagInfoList": []
            }
        ],
        "Total": 1,
        "RequestId": "462f39bb-229b-40b1-9114-bd52e13eb5e7"
    }
}
```

**Example 2: 预付费**



Input: 

```
tccli antiddos DescribeBgpInstances --cli-unfold-argument  \
    --FilterRegion ap-guangzhou \
    --FilterInstanceIdList bgp-000004rr
```

Output: 
```
{
    "Response": {
        "BGPInstanceList": [
            {
                "DryRun": false,
                "EnterprisePackageConfig": null,
                "InstanceChargePrepaid": {
                    "Period": 1,
                    "RenewFlag": "NOTIFY_AND_MANUAL_RENEW"
                },
                "InstanceChargeType": "PREPAID",
                "InstanceCount": 1,
                "InstanceId": "bgp-000004rr",
                "PackageType": "StandardPlus",
                "StandardPackageConfig": null,
                "StandardPlusPackageConfig": {
                    "Bandwidth": 50,
                    "ElasticBandwidthFlag": false,
                    "ProtectCount": "TWO_TIMES",
                    "ProtectIpCount": 10,
                    "Region": "ap-guangzhou"
                },
                "TagInfoList": []
            }
        ],
        "Total": 1,
        "RequestId": "a7f80029-ea53-466e-ab7b-dd6e4262a895"
    }
}
```

