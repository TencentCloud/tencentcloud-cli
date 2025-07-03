**Example 1: 查询套餐信息列表**

查询套餐信息列表,按照套餐生效时间排序，顺序为降序，从第0个套餐开始，拉取4个套餐信息。

Input: 

```
tccli teo DescribePlans --cli-unfold-argument  \
    --Offset 0 \
    --Limit 4 \
    --Order enable-time \
    --Direction desc
```

Output: 
```
{
    "Response": {
        "RequestId": "55496a31-e798-4aef-b40c-5cdbaef7fe6f",
        "Plans": [
            {
                "Area": "overseas",
                "AutoRenewal": false,
                "PayMode": 0,
                "PlanId": "edgeone-2ycvr8ml4zpq",
                "PlanType": "plan-enterprise-v2",
                "Status": "normal",
                "DDoSTrafficCapacity": 10000,
                "AccTrafficCapacity": 10000,
                "CrossMLCTrafficCapacity": 10000,
                "ExpiredTime": "2020-09-22T00:00:00Z",
                "EnabledTime": "2020-10-22T00:00:00Z",
                "SecRequestCapacity": 10000,
                "SecTrafficCapacity": 10000,
                "SmartTrafficCapacity": 10000,
                "L4TrafficCapacity": 10000,
                "SmartRequestCapacity": 10000,
                "VAUCapacity": 50,
                "ZonesInfo": [
                    {
                        "Paused": false,
                        "ZoneId": "zone-2ycvr8p31c5q",
                        "ZoneName": "edgeone.icu"
                    }
                ],
                "Bindable": "true"
            },
            {
                "Area": "global",
                "AutoRenewal": false,
                "PayMode": 0,
                "PlanId": "edgeone-2ycvr8p345am",
                "PlanType": "plan-enterprise-v2",
                "Status": "normal",
                "DDoSTrafficCapacity": 10000,
                "AccTrafficCapacity": 10000,
                "CrossMLCTrafficCapacity": 10000,
                "ExpiredTime": "2020-09-22T00:00:00Z",
                "EnabledTime": "2020-10-22T00:00:00Z",
                "SecRequestCapacity": 10000,
                "SecTrafficCapacity": 10000,
                "SmartTrafficCapacity": 10000,
                "L4TrafficCapacity": 10000,
                "SmartRequestCapacity": 10000,
                "VAUCapacity": 50,
                "ZonesInfo": [
                    {
                        "Paused": false,
                        "ZoneId": "zone-2ycvr8p35jv2",
                        "ZoneName": "edgeone.xyz"
                    }
                ],
                "Bindable": "true"
            },
            {
                "Area": "overseas",
                "AutoRenewal": false,
                "PayMode": 0,
                "PlanId": "edgeone-2ycvr8p36yfi",
                "PlanType": "plan-enterprise",
                "Status": "normal",
                "DDoSTrafficCapacity": 10000,
                "AccTrafficCapacity": 10000,
                "CrossMLCTrafficCapacity": 10000,
                "ExpiredTime": "2020-09-22T00:00:00Z",
                "EnabledTime": "2020-10-22T00:00:00Z",
                "SecRequestCapacity": 10000,
                "SecTrafficCapacity": 10000,
                "SmartTrafficCapacity": 10000,
                "L4TrafficCapacity": 10000,
                "SmartRequestCapacity": 10000,
                "VAUCapacity": 50,
                "ZonesInfo": [
                    {
                        "Paused": false,
                        "ZoneId": "zone-2ycvr8p38czy",
                        "ZoneName": "edgeone.com"
                    }
                ],
                "Bindable": "true"
            },
            {
                "Area": "overseas",
                "AutoRenewal": false,
                "PayMode": 0,
                "PlanId": "edgeone-2ycvr8p39rke",
                "PlanType": "plan-standard",
                "Status": "normal",
                "DDoSTrafficCapacity": 10000,
                "AccTrafficCapacity": 10000,
                "CrossMLCTrafficCapacity": 10000,
                "ExpiredTime": "2020-09-22T00:00:00Z",
                "EnabledTime": "2020-10-22T00:00:00Z",
                "SecRequestCapacity": 10000,
                "SecTrafficCapacity": 10000,
                "SmartTrafficCapacity": 10000,
                "L4TrafficCapacity": 10000,
                "SmartRequestCapacity": 10000,
                "VAUCapacity": 50,
                "ZonesInfo": [
                    {
                        "Paused": true,
                        "ZoneId": "zone-2vv6990bixl1",
                        "ZoneName": "edgeone.xyz"
                    }
                ],
                "Bindable": "false"
            }
        ],
        "TotalCount": 28
    }
}
```

