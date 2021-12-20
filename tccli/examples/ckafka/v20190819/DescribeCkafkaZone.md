**Example 1: 查看可用区列表**



Input: 

```
tccli ckafka DescribeCkafkaZone --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Result": {
            "ZoneList": [
                {
                    "ZoneId": "300001",
                    "IsInternalApp": 2,
                    "AppId": 1255613487,
                    "Flag": true,
                    "ZoneName": "香港一区",
                    "ZoneStatus": 4,
                    "Exflag": "1",
                    "SoldOut": "false",
                    "SalesInfo": [
                        {
                            "Platform": "xx",
                            "Flag": true,
                            "Version": "xx",
                            "SoldOut": true
                        }
                    ]
                },
                {
                    "ZoneId": "300002",
                    "IsInternalApp": 2,
                    "AppId": 1255613487,
                    "Flag": false,
                    "ZoneName": "香港二区",
                    "ZoneStatus": 4,
                    "Exflag": "1",
                    "SoldOut": "false",
                    "SalesInfo": [
                        {
                            "Platform": "xx",
                            "Flag": true,
                            "Version": "xx",
                            "SoldOut": true
                        }
                    ]
                },
                {
                    "ZoneId": "300003",
                    "IsInternalApp": 2,
                    "AppId": 1255613487,
                    "Flag": false,
                    "ZoneName": "香港三区",
                    "ZoneStatus": 4,
                    "Exflag": "1",
                    "SalesInfo": [
                        {
                            "Platform": "xx",
                            "Flag": true,
                            "Version": "xx",
                            "SoldOut": true
                        }
                    ],
                    "SoldOut": "true"
                }
            ],
            "MaxBuyInstanceNum": 20,
            "MaxBandwidth": 1200,
            "UnitPrice": {
                "RealTotalCost": 2.376,
                "TotalCost": 0
            },
            "MessagePrice": {
                "RealTotalCost": 0.18,
                "TotalCost": 0
            },
            "ClusterInfo": [],
            "Standard": "{}",
            "StandardS2": "{\"InstanceTypeConfigSet\":[{\"Type\":\"sv_ckafka_instance_s2_1\",\"Desc\":\"入门型\",\"Bandwidth\":320,\"DiskSize\":500,\"Pid\":15127,\"MaximumInstancePartition\":100,\"MaximumInstanceTopic\":40},{\"Type\":\"sv_ckafka_instance_s2_2\",\"Desc\":\"标准型\",\"Bandwidth\":800,\"DiskSize\":1500,\"Pid\":15128,\"MaximumInstancePartition\":160,\"MaximumInstanceTopic\":80},{\"Type\":\"sv_ckafka_instance_s2_3\",\"Desc\":\"进阶型\",\"Bandwidth\":1200,\"DiskSize\":3000,\"Pid\":15129,\"MaximumInstancePartition\":200,\"MaximumInstanceTopic\":100},{\"Type\":\"sv_ckafka_instance_s2_4\",\"Desc\":\"容量型\",\"Bandwidth\":1600,\"DiskSize\":4500,\"Pid\":15130,\"MaximumInstancePartition\":300,\"MaximumInstanceTopic\":150},{\"Type\":\"sv_ckafka_instance_s2_5\",\"Desc\":\"高阶型1\",\"Bandwidth\":2400,\"DiskSize\":6000,\"Pid\":15131,\"MaximumInstancePartition\":500,\"MaximumInstanceTopic\":250},{\"Type\":\"sv_ckafka_instance_s2_6\",\"Desc\":\"高阶型2\",\"Bandwidth\":3200,\"DiskSize\":8000,\"Pid\":15132,\"MaximumInstancePartition\":600,\"MaximumInstanceTopic\":300},{\"Type\":\"sv_ckafka_instance_s2_7\",\"Desc\":\"高阶型3\",\"Bandwidth\":4800,\"DiskSize\":10000,\"Pid\":15133,\"MaximumInstancePartition\":800,\"MaximumInstanceTopic\":400},{\"Type\":\"sv_ckafka_instance_s2_8\",\"Desc\":\"高阶型4\",\"Bandwidth\":7200,\"DiskSize\":12000,\"Pid\":15134,\"MaximumInstancePartition\":1000,\"MaximumInstanceTopic\":500}],\"maximumTopicPartition\":1000,\"maximumInstanceConsumerGroup\":0}\n",
            "Profession": "{\"BasicEdition\":{\"Bandwidth\":{\"Maximum\":1200,\"Minimal\":40,\"Step\":20},\"DiskCapacity\":{\"40\":{\"Maximum\":5000,\"Minimal\":500,\"Step\":100},\"120\":{\"Maximum\":10000,\"Minimal\":1000,\"Step\":100},\"320\":{\"Maximum\":30000,\"Minimal\":3000,\"Step\":100},\"620\":{\"Maximum\":54000,\"Minimal\":5400,\"Step\":100},\"920\":{\"Maximum\":75000,\"Minimal\":7500,\"Step\":100}},\"DiskTypes\":[\"SSD\",\"CLOUD_BASIC\"],\"MessageRetention\":{\"Maximum\":2160,\"Minimal\":24,\"Step\":1},\"Partition\":{\"40\":{\"Maximum\":1000,\"Minimal\":500,\"Step\":100},\"60\":{\"Maximum\":1200,\"Minimal\":600,\"Step\":100},\"120\":{\"Maximum\":1600,\"Minimal\":800,\"Step\":100},\"180\":{\"Maximum\":2000,\"Minimal\":1000,\"Step\":100},\"240\":{\"Maximum\":2400,\"Minimal\":1200,\"Step\":100},\"320\":{\"Maximum\":2800,\"Minimal\":1400,\"Step\":100},\"400\":{\"Maximum\":3200,\"Minimal\":1600,\"Step\":100},\"500\":{\"Maximum\":3600,\"Minimal\":1800,\"Step\":100},\"600\":{\"Maximum\":4000,\"Minimal\":2000,\"Step\":100},\"800\":{\"Maximum\":4500,\"Minimal\":2400,\"Step\":100},\"1000\":{\"Maximum\":5000,\"Minimal\":2800,\"Step\":100},\"1200\":{\"Maximum\":5500,\"Minimal\":3200,\"Step\":100}},\"Topic\":{\"40\":{\"Maximum\":100,\"Minimal\":50,\"Step\":1},\"60\":{\"Maximum\":120,\"Minimal\":60,\"Step\":1},\"120\":{\"Maximum\":160,\"Minimal\":80,\"Step\":1},\"180\":{\"Maximum\":200,\"Minimal\":100,\"Step\":1},\"240\":{\"Maximum\":240,\"Minimal\":120,\"Step\":1},\"320\":{\"Maximum\":280,\"Minimal\":160,\"Step\":1},\"400\":{\"Maximum\":320,\"Minimal\":200,\"Step\":1},\"500\":{\"Maximum\":360,\"Minimal\":240,\"Step\":1},\"600\":{\"Maximum\":400,\"Minimal\":280,\"Step\":1},\"800\":{\"Maximum\":450,\"Minimal\":320,\"Step\":1},\"1000\":{\"Maximum\":500,\"Minimal\":360,\"Step\":1},\"1200\":{\"Maximum\":550,\"Minimal\":400,\"Step\":1}}},\"HighPerformanceEdition\":{\"Bandwidth\":{\"Maximum\":3200,\"Minimal\":1600,\"Step\":400},\"DiskCapacity\":{\"1600\":{\"Maximum\":120000,\"Minimal\":12000,\"Step\":100},\"2000\":{\"Maximum\":160000,\"Minimal\":16000,\"Step\":100},\"2400\":{\"Maximum\":200000,\"Minimal\":20000,\"Step\":100},\"2800\":{\"Maximum\":240000,\"Minimal\":24000,\"Step\":100},\"3200\":{\"Maximum\":280000,\"Minimal\":28000,\"Step\":100}},\"DiskTypes\":[\"SSD\",\"CLOUD_BASIC\"],\"MessageRetention\":{\"Maximum\":2160,\"Minimal\":24,\"Step\":1},\"Partition\":{\"1600\":{\"Maximum\":6000,\"Minimal\":4000,\"Step\":100},\"2000\":{\"Maximum\":7000,\"Minimal\":4500,\"Step\":100},\"2400\":{\"Maximum\":8000,\"Minimal\":5000,\"Step\":100},\"2800\":{\"Maximum\":9000,\"Minimal\":5500,\"Step\":100},\"3200\":{\"Maximum\":10000,\"Minimal\":6000,\"Step\":100}},\"Topic\":{\"1600\":{\"Maximum\":600,\"Minimal\":500,\"Step\":1},\"2000\":{\"Maximum\":700,\"Minimal\":600,\"Step\":1},\"2400\":{\"Maximum\":800,\"Minimal\":700,\"Step\":1},\"2800\":{\"Maximum\":900,\"Minimal\":800,\"Step\":1},\"3200\":{\"Maximum\":1000,\"Minimal\":900,\"Step\":1}}}}",
            "Physical": "{}",
            "PublicNetwork": "{}",
            "PublicNetworkLimit": "{}"
        },
        "RequestId": "4831a936-0a03-408e-9ffc-a813a11ad769"
    }
}
```

