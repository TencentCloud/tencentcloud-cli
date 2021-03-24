**Example 1: 获取资源列表**



Input: 

```
tccli dayu DescribeResourceList --cli-unfold-argument  \
    --Business bgpip \
    --RegionList gz \
    --Line 1 \
    --IdList bgpip-000000001 \
    --IpList 3.3.3.3 \
    --Name "" \
    --Status 0 1 2 \
    --Expire 0 \
    --OderBy.0.Field bandwidth \
    --OderBy.0.Order DESC \
    --Limit 30 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "8466d9e1-70a9-4575-8e02-df15bd50bc49",
        "Business": "bgpip",
        "ServicePacks": [
            {
                "Record": [
                    {
                        "Key": "Id",
                        "Value": "net-0000000v"
                    },
                    {
                        "Key": "DdosMax",
                        "Value": "20000"
                    },
                    {
                        "Key": "ElasticLimit",
                        "Value": "0"
                    },
                    {
                        "Key": "AutoRenewFlag",
                        "Value": "0"
                    },
                    {
                        "Key": "DDoSLevel",
                        "Value": "middle"
                    },
                    {
                        "Key": "RuleLimit",
                        "Value": "60"
                    },
                    {
                        "Key": "DdosThreshold",
                        "Value": "0"
                    },
                    {
                        "Key": "CurrentRegion",
                        "Value": "bj"
                    },
                    {
                        "Key": "DdosOverload",
                        "Value": "0"
                    },
                    {
                        "Key": "CCMax",
                        "Value": "40000"
                    },
                    {
                        "Key": "CName",
                        "Value": "17fa9bb3.dayugslb.com"
                    },
                    {
                        "Key": "CreateTime",
                        "Value": "2018-09-26 21:39:55"
                    },
                    {
                        "Key": "IsolateTime",
                        "Value": "0000-00-00 00:00:00"
                    },
                    {
                        "Key": "Name",
                        "Value": "多少"
                    },
                    {
                        "Key": "OriginRegion",
                        "Value": "bj"
                    },
                    {
                        "Key": "CurrentGroup",
                        "Value": "100"
                    },
                    {
                        "Key": "ReturnHour",
                        "Value": "2"
                    },
                    {
                        "Key": "Expire",
                        "Value": "2018-10-26 21:39:55"
                    },
                    {
                        "Key": "ServiceBandwidth",
                        "Value": "100"
                    },
                    {
                        "Key": "CCEnabled",
                        "Value": "0"
                    },
                    {
                        "Key": "AutoReturn",
                        "Value": "1"
                    },
                    {
                        "Key": "CCThreshold",
                        "Value": "0"
                    },
                    {
                        "Key": "Status",
                        "Value": "idle"
                    },
                    {
                        "Key": "TransRules",
                        "Value": "0"
                    }
                ]
            }
        ],
        "Total": 1
    }
}
```

