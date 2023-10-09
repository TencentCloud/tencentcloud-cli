**Example 1: 示例**



Input: 

```
tccli cwp DescribeLogDeliveryKafkaOptions --cli-unfold-argument  \
    --InstanceID ckafka-ce80kte5
```

Output: 
```
{
    "Response": {
        "InstanceList": [
            {
                "InstanceID": "ckafka-ce80kte5",
                "InstanceName": "云镜测试环境",
                "KafkaVersion": "0.10.2.1",
                "DiskSize": 300,
                "VpcId": "",
                "SubnetId": "",
                "Healthy": 1,
                "Zone": "广州三区",
                "Az": "广州",
                "Bandwidth": 320,
                "TopicList": [
                    {
                        "TopicID": "topic-epj9w5yw",
                        "TopicName": "bruteforce_attack"
                    },
                    {
                        "TopicID": "topic-r48k6eym",
                        "TopicName": "create_snapshot"
                    },
                    {
                        "TopicID": "inter-topic-ncjmndfq",
                        "TopicName": "host_login"
                    },
                    {
                        "TopicID": "inter-topic-ngkulq16",
                        "TopicName": "host_login_by_area"
                    },
                    {
                        "TopicID": "inter-topic-pohpglie",
                        "TopicName": "json_event_msg"
                    },
                    {
                        "TopicID": "inter-topic-hs4eot1l",
                        "TopicName": "machines"
                    },
                    {
                        "TopicID": "topic-93sgsjva",
                        "TopicName": "malware"
                    },
                    {
                        "TopicID": "topic-p59qj43e",
                        "TopicName": "monitor_event"
                    },
                    {
                        "TopicID": "topic-a890z57e",
                        "TopicName": "network_attack"
                    },
                    {
                        "TopicID": "topic-rit2rzqu",
                        "TopicName": "network_attack_test"
                    },
                    {
                        "TopicID": "topic-kjqx02wm",
                        "TopicName": "priv_escalation"
                    },
                    {
                        "TopicID": "topic-71smzlj0",
                        "TopicName": "remote_task"
                    },
                    {
                        "TopicID": "topic-5eom87g4",
                        "TopicName": "reverse_shell"
                    },
                    {
                        "TopicID": "topic-jv0srr3y",
                        "TopicName": "tcss_events_notify"
                    },
                    {
                        "TopicID": "inter-topic-k3qc77wn",
                        "TopicName": "test"
                    },
                    {
                        "TopicID": "topic-7wn22bzw",
                        "TopicName": "vulner_detect_tmp"
                    },
                    {
                        "TopicID": "topic-9d5rjens",
                        "TopicName": "vulner_result"
                    },
                    {
                        "TopicID": "inter-topic-ioovdkb3",
                        "TopicName": "vul_upgrade_info"
                    }
                ],
                "RouteList": [
                    {
                        "RouteID": 5427,
                        "Domain": "",
                        "DomainPort": 0,
                        "Vip": "172.16.100.6:9092",
                        "VipType": 3,
                        "AccessType": 0
                    },
                    {
                        "RouteID": 99469,
                        "Domain": "",
                        "DomainPort": 0,
                        "Vip": "10.66.188.88:9092",
                        "VipType": 2,
                        "AccessType": 0
                    },
                    {
                        "RouteID": 106724,
                        "Domain": "",
                        "DomainPort": 0,
                        "Vip": "100.119.167.50:11368",
                        "VipType": 4,
                        "AccessType": 0
                    },
                    {
                        "RouteID": 126523,
                        "Domain": "",
                        "DomainPort": 0,
                        "Vip": "9.139.46.54:6007",
                        "VipType": 7,
                        "AccessType": 1
                    }
                ]
            }
        ],
        "RequestId": "3758d2c5-57d1-471a-b713-ad353665ce62"
    }
}
```

