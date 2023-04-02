**Example 1: 查询CCN地域出带宽详情**

该示例查询CCN地域出带宽详情，其中CCN的付费模式是后付费。后付费计费模式的CCN，用户不需要关注ExpireTime，RenewFlag参数。

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
                "TagSet": [
                    {
                        "Key": "test",
                        "Value": "123"
                    }
                ],
                "RegionFlowControlId": "fcr-krx0mfoi",
                "CreatedTime": "2020-05-20 16:29:44",
                "ExpiredTime": "2020-05-20 16:29:44",
                "MarketId": "abc",
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW"
            }
        ],
        "TotalCount": 1,
        "RequestId": "639c4bff-ff57-4734-bd72-f543df3b0771"
    }
}
```

**Example 2: 查询CCN地域间带宽详情**

该示例是查询CCN地域间带宽详情，云联网为预付费，其中返回两个地域间限速实例，限速实例fcr-crrnp6w4续费模式RenewFlag为NOTIFY_AND_MANUAL_RENEW（非自动续费），限速实例fcr-lnfsgh4y续费模式RenewFlag为NOTIFY_AND_AUTO_RENEW（自动续费）。

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
                "TagSet": [
                    {
                        "Key": "test",
                        "Value": "123"
                    }
                ],
                "RegionFlowControlId": "fcr-crrnp6w4",
                "CreatedTime": "2020-06-10 14:48:13",
                "ExpiredTime": "2020-07-10 15:47:05",
                "MarketId": "abc",
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
                "TagSet": [
                    {
                        "Key": "test",
                        "Value": "123"
                    }
                ],
                "RegionFlowControlId": "fcr-lnfsgh4y",
                "CreatedTime": "2020-06-10 15:55:29",
                "ExpiredTime": "2020-07-10 15:55:29",
                "MarketId": "abc",
                "RenewFlag": "NOTIFY_AND_AUTO_RENEW"
            }
        ],
        "TotalCount": 2,
        "RequestId": "39db643d-64ba-456b-91c6-279115682ad2"
    }
}
```

