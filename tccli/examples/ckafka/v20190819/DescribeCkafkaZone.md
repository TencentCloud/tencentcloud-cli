**Example 1: 查看可用区列表**



Input: 

```
tccli ckafka DescribeCkafkaZone --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "65192154-338c-4cd4-b3c0-1457dfdd2e4c",
        "Result": {
            "ClusterInfo": [],
            "ForceCheckTag": null,
            "Limit": null,
            "MaxBandwidth": 1200,
            "MaxBuyInstanceNum": 20,
            "MessagePrice": {
                "RealTotalCost": 0,
                "TotalCost": 0
            },
            "Offset": null,
            "Physical": "",
            "Profession": "{\"BasicEdition\":{\"Bandwidth\":{\"Maximum\":1200,\"Minimal\":20,\"Step\":20},\"DiskCapacity\":{\"20\":{\"Maximum\":500000,\"Minimal\":200,\"Step\":100},\"40\":{\"Maximum\":500000,\"Minimal\":500,\"Step\":100},\"120\":{\"Maximum\":500000,\"Minimal\":1000,\"Step\":100},\"320\":{\"Maximum\":500000,\"Minimal\":3000,\"Step\":100},\"800\":{\"Maximum\":500000,\"Minimal\":5400,\"Step\":100},\"1000\":{\"Maximum\":500000,\"Minimal\":7500,\"Step\":100}},\"DiskTypes\":[\"SSD\",\"CLOUD_BASIC\"],\"MessageRetention\":{\"Maximum\":2160,\"Minimal\":24,\"Step\":1},\"Partition\":{\"20\":{\"Maximum\":40000,\"Minimal\":400,\"Step\":100},\"40\":{\"Maximum\":40000,\"Minimal\":800,\"Step\":100},\"60\":{\"Maximum\":40000,\"Minimal\":900,\"Step\":100},\"120\":{\"Maximum\":40000,\"Minimal\":1200,\"Step\":100},\"180\":{\"Maximum\":40000,\"Minimal\":1400,\"Step\":100},\"240\":{\"Maximum\":40000,\"Minimal\":1600,\"Step\":100},\"320\":{\"Maximum\":40000,\"Minimal\":1800,\"Step\":100},\"400\":{\"Maximum\":40000,\"Minimal\":2000,\"Step\":100},\"500\":{\"Maximum\":40000,\"Minimal\":2200,\"Step\":100},\"600\":{\"Maximum\":40000,\"Minimal\":2400,\"Step\":100},\"800\":{\"Maximum\":40000,\"Minimal\":2600,\"Step\":100},\"1000\":{\"Maximum\":40000,\"Minimal\":2800,\"Step\":100},\"1200\":{\"Maximum\":40000,\"Minimal\":3200,\"Step\":100}}},\"HighPerformanceEdition\":{\"Bandwidth\":{\"Maximum\":100000,\"Minimal\":1600,\"Step\":200},\"DiskCapacity\":{\"1600\":{\"Maximum\":500000,\"Minimal\":10000,\"Step\":100},\"2000\":{\"Maximum\":500000,\"Minimal\":10000,\"Step\":100},\"2400\":{\"Maximum\":500000,\"Minimal\":10000,\"Step\":100},\"2800\":{\"Maximum\":500000,\"Minimal\":10000,\"Step\":100},\"3200\":{\"Maximum\":500000,\"Minimal\":10000,\"Step\":100}},\"DiskTypes\":[\"SSD\",\"CLOUD_BASIC\"],\"MessageRetention\":{\"Maximum\":2160,\"Minimal\":24,\"Step\":1},\"Partition\":{\"1600\":{\"Maximum\":40000,\"Minimal\":4000,\"Step\":100},\"2000\":{\"Maximum\":40000,\"Minimal\":4500,\"Step\":100},\"2400\":{\"Maximum\":40000,\"Minimal\":5000,\"Step\":100},\"2800\":{\"Maximum\":40000,\"Minimal\":5500,\"Step\":100},\"3200\":{\"Maximum\":40000,\"Minimal\":6000,\"Step\":100}}}}\n",
            "PublicNetwork": "[{\"Maximum\":198,\"Minimal\":3,\"step\":3}]",
            "PublicNetworkLimit": "{\"Maximum\":999,\"Minimal\":198,\"step\":3,\"minimalZoneIds\":[100001,100002,200001,300001,400001],\"unsupportedRegionId\":[32,78]}",
            "RequestId": null,
            "Standard": "",
            "StandardS2": "{\"InstanceTypeConfigSet\":[{\"Type\":\"sv_ckafka_instance_s2_1\",\"Desc\":\"入门型\",\"DescEn\":\"Small\",\"Bandwidth\":320,\"MinDiskSize\":300,\"MaxDiskSize\":1000,\"DiskSize\":500,\"Pid\":1004034,\"MaximumInstancePartition\":60,\"MaximumInstanceTopic\":25},{\"Type\":\"sv_ckafka_instance_s2_2\",\"Desc\":\"标准型\",\"DescEn\":\"Standard\",\"Bandwidth\":800,\"DiskSize\":1500,\"MinDiskSize\":500,\"MaxDiskSize\":2500,\"Pid\":1004037,\"MaximumInstancePartition\":100,\"MaximumInstanceTopic\":40},{\"Type\":\"sv_ckafka_instance_s2_3\",\"Desc\":\"进阶型\",\"DescEn\":\"Advanced\",\"Bandwidth\":1200,\"DiskSize\":3000,\"MinDiskSize\":1000,\"MaxDiskSize\":4000,\"Pid\":1004038,\"MaximumInstancePartition\":150,\"MaximumInstanceTopic\":50}],\"maximumTopicPartition\":2500,\"maximumInstanceConsumerGroup\":0}",
            "UnitPrice": {
                "RealTotalCost": 0,
                "TotalCost": 0
            },
            "Version": null,
            "ZoneList": [
                {
                    "AppId": 1300957330,
                    "ExtraFlag": "1",
                    "Flag": true,
                    "IsInternalApp": 1,
                    "SalesInfo": [
                        {
                            "Flag": true,
                            "Platform": "standard",
                            "SoldOut": true,
                            "Version": "0.10.2.1"
                        },
                        {
                            "Flag": true,
                            "Platform": "standard",
                            "SoldOut": true,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "0.10.2"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "3.2.3"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": true,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": true,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": true,
                            "Version": "3.2.3"
                        }
                    ],
                    "SoldOut": "true",
                    "ZoneId": "800001",
                    "ZoneName": "北京一区",
                    "ZoneStatus": 4
                },
                {
                    "AppId": 1300957330,
                    "ExtraFlag": "0",
                    "Flag": false,
                    "IsInternalApp": 1,
                    "SalesInfo": [
                        {
                            "Flag": false,
                            "Platform": "standard",
                            "SoldOut": true,
                            "Version": "0.10.2.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "standard",
                            "SoldOut": true,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "0.10.2"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "3.2.3"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": true,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": true,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": true,
                            "Version": "3.2.3"
                        }
                    ],
                    "SoldOut": "true",
                    "ZoneId": "800002",
                    "ZoneName": "北京二区",
                    "ZoneStatus": 3
                },
                {
                    "AppId": 1300957330,
                    "ExtraFlag": "0",
                    "Flag": false,
                    "IsInternalApp": 1,
                    "SalesInfo": [
                        {
                            "Flag": false,
                            "Platform": "standard",
                            "SoldOut": false,
                            "Version": "0.10.2.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "standard",
                            "SoldOut": true,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "0.10.2"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "3.2.3"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": false,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": false,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": false,
                            "Version": "3.2.3"
                        }
                    ],
                    "SoldOut": "false",
                    "ZoneId": "800003",
                    "ZoneName": "北京三区",
                    "ZoneStatus": 3
                },
                {
                    "AppId": 1300957330,
                    "ExtraFlag": "0",
                    "Flag": false,
                    "IsInternalApp": 1,
                    "SalesInfo": [
                        {
                            "Flag": false,
                            "Platform": "standard",
                            "SoldOut": false,
                            "Version": "0.10.2.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "standard",
                            "SoldOut": false,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "0.10.2"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "3.2.3"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": true,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": true,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": true,
                            "Version": "3.2.3"
                        }
                    ],
                    "SoldOut": "true",
                    "ZoneId": "800004",
                    "ZoneName": "北京四区",
                    "ZoneStatus": 3
                },
                {
                    "AppId": 1300957330,
                    "ExtraFlag": "0",
                    "Flag": false,
                    "IsInternalApp": 1,
                    "SalesInfo": [
                        {
                            "Flag": false,
                            "Platform": "standard",
                            "SoldOut": false,
                            "Version": "0.10.2.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "standard",
                            "SoldOut": false,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "0.10.2"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": true,
                            "Version": "3.2.3"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": true,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": true,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": true,
                            "Version": "3.2.3"
                        }
                    ],
                    "SoldOut": "true",
                    "ZoneId": "800005",
                    "ZoneName": "北京五区",
                    "ZoneStatus": 3
                },
                {
                    "AppId": 1300957330,
                    "ExtraFlag": "0",
                    "Flag": false,
                    "IsInternalApp": 1,
                    "SalesInfo": [
                        {
                            "Flag": false,
                            "Platform": "standard",
                            "SoldOut": false,
                            "Version": "0.10.2.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "standard",
                            "SoldOut": false,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "0.10.2"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "3.2.3"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": false,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": false,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": false,
                            "Version": "3.2.3"
                        }
                    ],
                    "SoldOut": "false",
                    "ZoneId": "800006",
                    "ZoneName": "北京六区",
                    "ZoneStatus": 3
                },
                {
                    "AppId": 1300957330,
                    "ExtraFlag": "0",
                    "Flag": false,
                    "IsInternalApp": 1,
                    "SalesInfo": [
                        {
                            "Flag": false,
                            "Platform": "standard",
                            "SoldOut": false,
                            "Version": "0.10.2.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "standard",
                            "SoldOut": false,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "0.10.2"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "3.2.3"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": false,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": false,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": false,
                            "Version": "3.2.3"
                        }
                    ],
                    "SoldOut": "false",
                    "ZoneId": "800007",
                    "ZoneName": "北京七区",
                    "ZoneStatus": 3
                },
                {
                    "AppId": 1300957330,
                    "ExtraFlag": "1",
                    "Flag": true,
                    "IsInternalApp": 1,
                    "SalesInfo": [
                        {
                            "Flag": true,
                            "Platform": "standard",
                            "SoldOut": true,
                            "Version": "0.10.2.1"
                        },
                        {
                            "Flag": true,
                            "Platform": "standard",
                            "SoldOut": true,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "0.10.2"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "3.2.3"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": false,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": false,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": false,
                            "Version": "3.2.3"
                        }
                    ],
                    "SoldOut": "false",
                    "ZoneId": "2000800004",
                    "ZoneName": "腾讯地图CDZ北京一区",
                    "ZoneStatus": 4
                },
                {
                    "AppId": 1300957330,
                    "ExtraFlag": "0",
                    "Flag": false,
                    "IsInternalApp": 1,
                    "SalesInfo": [
                        {
                            "Flag": false,
                            "Platform": "standard",
                            "SoldOut": true,
                            "Version": "0.10.2.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "standard",
                            "SoldOut": true,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "0.10.2"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "1.1.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "profession",
                            "SoldOut": false,
                            "Version": "3.2.3"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": false,
                            "Version": "2.4.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": false,
                            "Version": "2.8.1"
                        },
                        {
                            "Flag": false,
                            "Platform": "premium",
                            "SoldOut": false,
                            "Version": "3.2.3"
                        }
                    ],
                    "SoldOut": "false",
                    "ZoneId": "800008",
                    "ZoneName": "北京八区",
                    "ZoneStatus": 3
                }
            ]
        }
    }
}
```

