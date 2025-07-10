**Example 1: 实例套餐列表**

实例套餐列表

Input: 

```
tccli igtm DescribeInstancePackageList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "AutoRenewFlag": 1,
                "CostItemList": [],
                "CreateTime": "2024-03-27 14:08:03",
                "CurrentDeadline": "2024-04-27 14:08:03",
                "InstanceId": "",
                "InstanceName": "",
                "IsExpire": 0,
                "MinCheckInterval": 60,
                "MinGlobalTtl": 60,
                "PackageType": "STANDARD",
                "Remark": "",
                "ResourceId": "gtm-pdnssdbxdst",
                "ScheduleStrategy": [
                    "LOCATION",
                    "DELAY"
                ],
                "Status": "ENABLED",
                "TrafficStrategy": [
                    "ALL",
                    "WEIGHT"
                ]
            },
            {
                "AutoRenewFlag": 0,
                "CostItemList": [
                    {
                        "CostName": "sv_igtm_standard_instance",
                        "CostValue": 1
                    }
                ],
                "CreateTime": "2024-03-27 09:55:06",
                "CurrentDeadline": "2025-04-27 09:55:07",
                "InstanceId": "gtm-axjpoifqwev",
                "InstanceName": "gjz-测试",
                "IsExpire": 0,
                "MinCheckInterval": 60,
                "MinGlobalTtl": 60,
                "PackageType": "STANDARD",
                "Remark": "",
                "ResourceId": "gtm-rznpntnbzov",
                "ScheduleStrategy": [
                    "LOCATION",
                    "DELAY"
                ],
                "Status": "ENABLED",
                "TrafficStrategy": [
                    "ALL",
                    "WEIGHT"
                ]
            }
        ],
        "RequestId": "d90cae16-82b5-481c-bc1b-3e11ee829d50",
        "TotalCount": 2
    }
}
```

