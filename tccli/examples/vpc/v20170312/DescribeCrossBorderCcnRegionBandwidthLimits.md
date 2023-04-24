**Example 1: 无入参查询**

无入参查询云联网跨境限速实例

Input: 

```
tccli vpc DescribeCrossBorderCcnRegionBandwidthLimits --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CcnBandwidthSet": [
            {
                "CcnId": "ccn-025qoqpx",
                "CreatedTime": "2020-07-30 15:32:27",
                "ExpiredTime": "2021-01-30 15:32:27",
                "UpdateTime": "2022-03-07 12:36:17",
                "RegionFlowControlId": "fcr-1duimd7w",
                "MarketId": "",
                "UserAccountID": "3436874624",
                "IsCrossBorder": true,
                "IsSecurityLock": false,
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "InstanceChargeType": "",
                "CcnRegionBandwidthLimit": {
                    "SourceRegion": "ap-guangzhou",
                    "DestinationRegion": "ap-hongkong",
                    "BandwidthLimit": 0
                }
            },
            {
                "CcnId": "ccn-qhmusb7r",
                "CreatedTime": "2020-07-31 17:52:41",
                "ExpiredTime": "2020-11-30 17:52:41",
                "UpdateTime": "2022-03-07 12:36:17",
                "RegionFlowControlId": "fcr-n8d6es84",
                "MarketId": "market-o9zkna2cc",
                "UserAccountID": "979137",
                "IsCrossBorder": true,
                "IsSecurityLock": false,
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "InstanceChargeType": "",
                "CcnRegionBandwidthLimit": {
                    "SourceRegion": "ap-shanghai",
                    "DestinationRegion": "ap-hongkong",
                    "BandwidthLimit": 0
                }
            },
            {
                "CcnId": "ccn-cdnjw6bv",
                "CreatedTime": "2020-08-02 13:29:47",
                "ExpiredTime": "2020-11-02 13:29:47",
                "UpdateTime": "2022-03-07 12:36:17",
                "RegionFlowControlId": "fcr-frs5y7mo",
                "MarketId": "market-4rvy8k8eo",
                "UserAccountID": "3436874624",
                "IsCrossBorder": true,
                "IsSecurityLock": false,
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "InstanceChargeType": "",
                "CcnRegionBandwidthLimit": {
                    "SourceRegion": "ap-guangzhou",
                    "DestinationRegion": "ap-hongkong",
                    "BandwidthLimit": 2
                }
            },
            {
                "CcnId": "ccn-qhmusb7r",
                "CreatedTime": "2020-08-02 14:35:38",
                "ExpiredTime": "2020-09-02 14:35:38",
                "UpdateTime": "2022-03-07 12:36:17",
                "RegionFlowControlId": "fcr-gvbhcaec",
                "MarketId": "market-ibxg5q2ey",
                "UserAccountID": "979137",
                "IsCrossBorder": true,
                "IsSecurityLock": false,
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "InstanceChargeType": "",
                "CcnRegionBandwidthLimit": {
                    "SourceRegion": "ap-guangzhou",
                    "DestinationRegion": "ap-hongkong",
                    "BandwidthLimit": 0
                }
            },
            {
                "CcnId": "ccn-cdnjw6bv",
                "CreatedTime": "2020-08-12 16:10:09",
                "ExpiredTime": "2021-01-12 16:10:09",
                "UpdateTime": "2022-03-07 12:36:17",
                "RegionFlowControlId": "fcr-d7vklnwm",
                "MarketId": "market-0gctjva40",
                "UserAccountID": "3436874624",
                "IsCrossBorder": true,
                "IsSecurityLock": false,
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "InstanceChargeType": "",
                "CcnRegionBandwidthLimit": {
                    "SourceRegion": "ap-hongkong",
                    "DestinationRegion": "ap-beijing",
                    "BandwidthLimit": 0
                }
            },
            {
                "CcnId": "ccn-q64rvk9x",
                "CreatedTime": "2020-08-14 10:54:15",
                "ExpiredTime": "2020-09-14 10:54:15",
                "UpdateTime": "2022-03-07 12:36:17",
                "RegionFlowControlId": "fcr-9uhfrbj8",
                "MarketId": "market-judfoon5c",
                "UserAccountID": "1742152960",
                "IsCrossBorder": true,
                "IsSecurityLock": false,
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "InstanceChargeType": "",
                "CcnRegionBandwidthLimit": {
                    "SourceRegion": "ap-hongkong",
                    "DestinationRegion": "ap-guangzhou",
                    "BandwidthLimit": 0
                }
            },
            {
                "CcnId": "ccn-bwt4g84j",
                "CreatedTime": "2020-08-17 15:21:30",
                "ExpiredTime": "2020-09-17 15:21:30",
                "UpdateTime": "2022-03-07 12:36:17",
                "RegionFlowControlId": "fcr-cotqwlu2",
                "MarketId": "market-626fzd912",
                "UserAccountID": "807348637",
                "IsCrossBorder": true,
                "IsSecurityLock": false,
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "InstanceChargeType": "",
                "CcnRegionBandwidthLimit": {
                    "SourceRegion": "ap-hongkong",
                    "DestinationRegion": "ap-beijing",
                    "BandwidthLimit": 0
                }
            },
            {
                "CcnId": "ccn-dp8rjtnn",
                "CreatedTime": "2020-08-21 11:40:50",
                "ExpiredTime": "2020-08-19 11:40:50",
                "UpdateTime": "2022-03-07 12:36:17",
                "RegionFlowControlId": "fcr-1hmgsj62",
                "MarketId": "",
                "UserAccountID": "1742152960",
                "IsCrossBorder": true,
                "IsSecurityLock": false,
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "InstanceChargeType": "",
                "CcnRegionBandwidthLimit": {
                    "SourceRegion": "ap-guangzhou",
                    "DestinationRegion": "ap-hongkong",
                    "BandwidthLimit": 0
                }
            },
            {
                "CcnId": "ccn-qd9rws31",
                "CreatedTime": "2020-08-21 12:31:52",
                "ExpiredTime": "2020-09-21 12:37:02",
                "UpdateTime": "2022-03-07 12:36:17",
                "RegionFlowControlId": "fcr-a5uhb60a",
                "MarketId": "market-1rhwihsnw",
                "UserAccountID": "1742152960",
                "IsCrossBorder": true,
                "IsSecurityLock": false,
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "InstanceChargeType": "",
                "CcnRegionBandwidthLimit": {
                    "SourceRegion": "ap-shanghai",
                    "DestinationRegion": "ap-hongkong",
                    "BandwidthLimit": 3
                }
            },
            {
                "CcnId": "ccn-qd9rws31",
                "CreatedTime": "2020-08-28 09:27:55",
                "ExpiredTime": "2020-09-28 09:27:55",
                "UpdateTime": "2022-03-07 12:36:17",
                "RegionFlowControlId": "fcr-488xjj38",
                "MarketId": "",
                "UserAccountID": "1742152960",
                "IsCrossBorder": true,
                "IsSecurityLock": false,
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "InstanceChargeType": "",
                "CcnRegionBandwidthLimit": {
                    "SourceRegion": "ap-guangzhou",
                    "DestinationRegion": "ap-hongkong",
                    "BandwidthLimit": 1
                }
            },
            {
                "CcnId": "ccn-3wgiiipt",
                "CreatedTime": "2022-03-09 13:56:24",
                "ExpiredTime": "2022-03-09 13:56:24",
                "UpdateTime": "2022-03-09 13:58:03",
                "RegionFlowControlId": "fcr-lo5dfhe6",
                "MarketId": "",
                "UserAccountID": "979137",
                "IsCrossBorder": true,
                "IsSecurityLock": false,
                "RenewFlag": "NOTIFY_AND_AUTO_RENEW",
                "InstanceChargeType": "",
                "CcnRegionBandwidthLimit": {
                    "SourceRegion": "ap-guangzhou",
                    "DestinationRegion": "ap-hongkong",
                    "BandwidthLimit": 20
                }
            }
        ],
        "TotalCount": 14,
        "RequestId": "405d200b-ad2a-486d-9541-d5f47a506827"
    }
}
```

**Example 2: 根据云联网ID查询**

根据云联网ID查询云联网跨境限速实例

Input: 

```
tccli vpc DescribeCrossBorderCcnRegionBandwidthLimits --cli-unfold-argument  \
    --Filters.0.Values ccn-025qoqpx \
    --Filters.0.Name ccn-ids
```

Output: 
```
{
    "Response": {
        "CcnBandwidthSet": [
            {
                "CcnId": "ccn-025qoqpx",
                "CreatedTime": "2020-07-30 15:32:27",
                "ExpiredTime": "2021-01-30 15:32:27",
                "UpdateTime": "2022-03-07 12:36:17",
                "RegionFlowControlId": "fcr-1duimd7w",
                "MarketId": "",
                "UserAccountID": "3436874624",
                "IsCrossBorder": true,
                "IsSecurityLock": false,
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "InstanceChargeType": "",
                "CcnRegionBandwidthLimit": {
                    "SourceRegion": "ap-guangzhou",
                    "DestinationRegion": "ap-hongkong",
                    "BandwidthLimit": 0
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "8ef886fc-e394-4eba-8da6-b1ae8f88fe61"
    }
}
```

**Example 3: 根据账户ID查询**

根据账户ID查询云联网跨境限速实例

Input: 

```
tccli vpc DescribeCrossBorderCcnRegionBandwidthLimits --cli-unfold-argument  \
    --Filters.0.Values 3436874624 \
    --Filters.0.Name user-account-id
```

Output: 
```
{
    "Response": {
        "CcnBandwidthSet": [
            {
                "CcnId": "ccn-025qoqpx",
                "CreatedTime": "2020-07-30 15:32:27",
                "ExpiredTime": "2021-01-30 15:32:27",
                "UpdateTime": "2022-03-07 12:36:17",
                "RegionFlowControlId": "fcr-1duimd7w",
                "MarketId": "",
                "UserAccountID": "3436874624",
                "IsCrossBorder": true,
                "IsSecurityLock": false,
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "InstanceChargeType": "",
                "CcnRegionBandwidthLimit": {
                    "SourceRegion": "ap-guangzhou",
                    "DestinationRegion": "ap-hongkong",
                    "BandwidthLimit": 0
                }
            },
            {
                "CcnId": "ccn-cdnjw6bv",
                "CreatedTime": "2020-08-02 13:29:47",
                "ExpiredTime": "2020-11-02 13:29:47",
                "UpdateTime": "2022-03-07 12:36:17",
                "RegionFlowControlId": "fcr-frs5y7mo",
                "MarketId": "market-4rvy8k8eo",
                "UserAccountID": "3436874624",
                "IsCrossBorder": true,
                "IsSecurityLock": false,
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "InstanceChargeType": "",
                "CcnRegionBandwidthLimit": {
                    "SourceRegion": "ap-guangzhou",
                    "DestinationRegion": "ap-hongkong",
                    "BandwidthLimit": 2
                }
            },
            {
                "CcnId": "ccn-cdnjw6bv",
                "CreatedTime": "2020-08-12 16:10:09",
                "ExpiredTime": "2021-01-12 16:10:09",
                "UpdateTime": "2022-03-07 12:36:17",
                "RegionFlowControlId": "fcr-d7vklnwm",
                "MarketId": "market-0gctjva40",
                "UserAccountID": "3436874624",
                "IsCrossBorder": true,
                "IsSecurityLock": false,
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "InstanceChargeType": "",
                "CcnRegionBandwidthLimit": {
                    "SourceRegion": "ap-hongkong",
                    "DestinationRegion": "ap-beijing",
                    "BandwidthLimit": 0
                }
            }
        ],
        "TotalCount": 3,
        "RequestId": "a5cf93d0-d717-4e89-8a51-e1418b43d9f9"
    }
}
```

