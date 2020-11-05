**Example 1: Querying the outbound bandwidth limits of a CCN**

This example shows you how to query the outbound bandwidth limits of a pay-as-you-go CCN, for which the `ExpireTime` and `RenewFlag` parameters can be ignored.

Input: 

```
tccli vpc GetCcnRegionBandwidthLimits --cli-unfold-argument  \
    --CcnId ccn-1pdchck1
```

Output: 
```
{
    "Response": {
        "CcnBandwidthSet": [
            {
                "CcnRegionBandwidthLimit": {
                    "Region": "ap-guangzhou",
                    "IsBm": false,
                    "BandwidthLimit": 10
                },
                "CcnId": "ccn-1pdchck1",
                "RegionFlowControlId": "fcr-krx0mfoi",
                "CreateTime": "2020-05-20 16:29:44",
                "ExpireTime": "2020-05-20 16:29:44",
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW"
            }
        ],
        "TotalCount": 1,
        "RequestId": "639c4bff-ff57-4734-bd72-f543df3b0771"
    }
}
```

**Example 2: Querying the inter-region bandwidth limits of a CCN**

This example shows you how to query the cross-region outbound bandwidths for monthly-subscribed CCN and obtain two instances with a cross-region bandwidth limit. The `fcr-crrnp6w4` instance has `NOTIFY_AND_MANUAL_RENEW` (no auto-renewal) for the `RenewFlag` parameter, and the `fcr-lnfsgh4y` instance has `NOTIFY_AND_AUTO_RENEW` (auto-renewal) for the `RenewFlag` parameter.

Input: 

```
tccli vpc GetCcnRegionBandwidthLimits --cli-unfold-argument  \
    --CcnId ccn-2gxeenq2
```

Output: 
```
{
    "Response": {
        "CcnBandwidthSet": [
            {
                "CcnRegionBandwidthLimit": {
                    "Region": "ap-guangzhou",
                    "IsBm": false,
                    "BandwidthLimit": 1,
                    "DstRegion": "ap-shanghai",
                    "DstIsBm": false
                },
                "CcnId": "ccn-2gxeenq2",
                "RegionFlowControlId": "fcr-crrnp6w4",
                "CreateTime": "2020-06-10 14:48:13",
                "ExpireTime": "2020-07-10 15:47:05",
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW"
            },
            {
                "CcnRegionBandwidthLimit": {
                    "Region": "ap-nanjing",
                    "IsBm": false,
                    "BandwidthLimit": 1,
                    "DstRegion": "ap-chengdu",
                    "DstIsBm": false
                },
                "CcnId": "ccn-2gxeenq2",
                "RegionFlowControlId": "fcr-lnfsgh4y",
                "CreateTime": "2020-06-10 15:55:29",
                "ExpireTime": "2020-07-10 15:55:29",
                "RenewFlag": "NOTIFY_AND_AUTO_RENEW"
            }
        ],
        "TotalCount": 2,
        "RequestId": "39db643d-64ba-456b-91c6-279115682ad2"
    }
}
```

