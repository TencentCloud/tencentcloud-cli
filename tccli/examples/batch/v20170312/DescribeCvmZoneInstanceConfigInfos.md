**Example 1: 查看重庆一区按量计费机型配置信息**



Input: 

```
tccli batch DescribeCvmZoneInstanceConfigInfos --cli-unfold-argument  \
    --Filters.0.Name zone \
    --Filters.0.Values ap-chongqing-1 \
    --Filters.1.Name instance-charge-type \
    --Filters.1.Values POSTPAID_BY_HOUR
```

Output: 
```
{
    "Response": {
        "InstanceTypeQuotaSet": [
            {
                "Status": "SELL",
                "Zone": "ap-chongqing-1",
                "NetworkCard": 0,
                "Price": {
                    "UnitPrice": 0.18,
                    "ChargeUnit": "HOUR"
                },
                "InstanceFamily": "S3",
                "Externals": {},
                "Cpu": 1,
                "TypeName": "标准型S3",
                "InstanceChargeType": "POSTPAID_BY_HOUR",
                "Memory": 1,
                "LocalDiskTypeList": [],
                "InstanceType": "S3.SMALL1"
            },
            {
                "Status": "SELL",
                "Zone": "ap-chongqing-1",
                "NetworkCard": 0,
                "Price": {
                    "UnitPrice": 0.26,
                    "ChargeUnit": "HOUR"
                },
                "InstanceFamily": "S3",
                "Externals": {},
                "Cpu": 1,
                "TypeName": "标准型S3",
                "InstanceChargeType": "POSTPAID_BY_HOUR",
                "Memory": 2,
                "LocalDiskTypeList": [],
                "InstanceType": "S3.SMALL2"
            }
        ],
        "RequestId": "2fba5b9c-e4ee-47ad-a776-dabb79ff2c35"
    }
}
```

