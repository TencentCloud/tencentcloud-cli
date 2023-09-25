**Example 1: 查询用户站点信息列表**

精确查询站点名称为“example.com”的站点信息。

Input: 

```
tccli teo DescribeZones --cli-unfold-argument  \
    --Filters.0.Name zone-name \
    --Filters.0.Values example.com \
    --Filters.0.Fuzzy False
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Zones": [
            {
                "ZoneId": "zone-2noz3g48ev6k",
                "ZoneName": "example.com",
                "ActiveStatus": "inactive",
                "AliasZoneName": "",
                "Area": "global",
                "CnameSpeedUp": "enabled",
                "CnameStatus": "pending",
                "CreatedOn": "2023-09-18T07:41:05Z",
                "IsFake": 0,
                "LockStatus": "enable",
                "ModifiedOn": "2023-09-18T07:41:50Z",
                "NameServers": [
                    "ns1.teodns.com.",
                    "ns2.teodns.com."
                ],
                "OriginalNameServers": [
                    "ns1.example.com.",
                    "ns2.example.com."
                ],
                "Paused": false,
                "Resources": [
                    {
                        "Area": "global",
                        "AutoRenewFlag": 0,
                        "CreateTime": "2023-09-18T07:41:18Z",
                        "EnableTime": "2023-09-18T07:41:18Z",
                        "ExpireTime": "2099-12-31T15:59:59Z",
                        "Group": "plan",
                        "Id": "edgeone-2noz3qqkvqth",
                        "PayMode": 0,
                        "PlanId": "edgeone-2noz3qqkvqth",
                        "Status": "normal",
                        "Sv": [
                            {
                                "Key": "sv_edgeone_plan_sec_ent_flatfee_cm",
                                "Value": "1",
                                "InstanceId": "",
                                "Pack": "",
                                "ProtectionSpecs": ""
                            }
                        ]
                    },
                    {
                        "Area": "global",
                        "AutoRenewFlag": 0,
                        "CreateTime": "2023-09-18T07:41:18Z",
                        "EnableTime": "2023-09-18T07:41:18Z",
                        "ExpireTime": "2099-12-31T15:59:59Z",
                        "Group": "pay-as-you-go",
                        "Id": "edgeone-2noz3t4be7xw",
                        "PayMode": 0,
                        "PlanId": "edgeone-2noz3qqkvqth",
                        "Status": "normal",
                        "Sv": [
                            {
                                "Key": "sv_edgeone_sec_request_queries_month",
                                "Value": "1",
                                "InstanceId": "",
                                "Pack": "",
                                "ProtectionSpecs": ""
                            },
                            {
                                "Key": "sv_edgeone_va_unit_month",
                                "Value": "1",
                                "InstanceId": "",
                                "Pack": "",
                                "ProtectionSpecs": ""
                            }
                        ]
                    }
                ],
                "Status": "pending",
                "Tags": [],
                "Type": "full",
                "VanityNameServers": null,
                "VanityNameServersIps": []
            }
        ],
        "RequestId": "641a08e3-2ef7-407c-9c2f-2a9928741df5"
    }
}
```

