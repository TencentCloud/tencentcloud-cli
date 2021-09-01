**Example 1: 获取操作日志**



Input: 

```
tccli dayu DescribeActionLog --cli-unfold-argument  \
    --StartTime '2018-11-23 00:00:00' \
    --EndTime '2018-11-24 00:00:00' \
    --Business bgpip \
    --Id bgpip-000000xe \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Record": [
                    {
                        "Key": "AppId",
                        "Value": "251000862"
                    },
                    {
                        "Key": "Uin",
                        "Value": "1445149556"
                    },
                    {
                        "Key": "Business",
                        "Value": "bgp"
                    },
                    {
                        "Key": "RsIdStr",
                        "Value": "bgp-0000000o"
                    },
                    {
                        "Key": "Action",
                        "Value": "NS.BGP.ServicePack.SetCCThreshold"
                    },
                    {
                        "Key": "ActionDesc",
                        "Value": "Set CC Threshold"
                    },
                    {
                        "Key": "Params",
                        "Value": "{\"id\":\"bgp-0000000o\",\"threshold\":\"850\"}"
                    },
                    {
                        "Key": "RespCode",
                        "Value": "success"
                    },
                    {
                        "Key": "Timestamp",
                        "Value": "2018-11-23 11:46:47"
                    }
                ]
            }
        ],
        "RequestId": "c451fdf9-d24d-4578-a40c-fe34e34829db",
        "TotalCount": 1
    }
}
```

