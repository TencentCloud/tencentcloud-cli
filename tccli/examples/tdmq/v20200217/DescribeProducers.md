**Example 1: 获取生产者列表**



Input: 

```
tccli tdmq DescribeProducers --cli-unfold-argument  \
    --EnvironmentId default \
    --TopicName U_TOPIC_nfa_game_push_retry_kb \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ProducerSets": [
            {
                "EnvironmentId": "default",
                "TopicName": "U_TOPIC_nfa_game_push_retry_kb",
                "CountConnect": 6,
                "ConnectionSets": [
                    {
                        "Address": "127.0.0.1:41062",
                        "Partitions": 1,
                        "ClientVersion": "",
                        "ProducerName": "sandbox-cluster-1-119-53_sandbox-cluster-1-120-1347_sandbox-cluster-1-121-34_sandbox-cluster-1-122-54",
                        "ProducerId": "5",
                        "AverageMsgSize": "0.0",
                        "MsgThroughputIn": "0.0"
                    },
                    {
                        "Address": "127.0.0.1:41062",
                        "Partitions": 0,
                        "ClientVersion": "",
                        "ProducerName": "sandbox-cluster-1-119-54_sandbox-cluster-1-120-1296_sandbox-cluster-1-121-24_sandbox-cluster-1-122-55",
                        "ProducerId": "8",
                        "AverageMsgSize": "0.0",
                        "MsgThroughputIn": "0.0"
                    },
                    {
                        "Address": "127.0.0.1:41062",
                        "Partitions": 5,
                        "ClientVersion": "",
                        "ProducerName": "sandbox-cluster-1-120-61_sandbox-cluster-1-120-1373_sandbox-cluster-1-121-0_sandbox-cluster-1-122-50",
                        "ProducerId": "2",
                        "AverageMsgSize": "0.0",
                        "MsgThroughputIn": "0.0"
                    },
                    {
                        "Address": "127.0.0.1:41062",
                        "Partitions": 3,
                        "ClientVersion": "",
                        "ProducerName": "sandbox-cluster-1-120-62_sandbox-cluster-1-120-1324_sandbox-cluster-1-121-27_sandbox-cluster-1-122-49",
                        "ProducerId": "4",
                        "AverageMsgSize": "0.0",
                        "MsgThroughputIn": "0.0"
                    },
                    {
                        "Address": "127.0.0.1:41062",
                        "Partitions": 7,
                        "ClientVersion": "",
                        "ProducerName": "sandbox-cluster-1-120-63_sandbox-cluster-1-120-1371_sandbox-cluster-1-121-23_sandbox-cluster-1-122-41",
                        "ProducerId": "1",
                        "AverageMsgSize": "0.0",
                        "MsgThroughputIn": "0.0"
                    },
                    {
                        "Address": "127.0.0.1:41062",
                        "Partitions": 6,
                        "ClientVersion": "",
                        "ProducerName": "sandbox-cluster-1-120-64_sandbox-cluster-1-120-1321_sandbox-cluster-1-121-65_sandbox-cluster-1-122-45",
                        "ProducerId": "6",
                        "AverageMsgSize": "0.0",
                        "MsgThroughputIn": "0.0"
                    }
                ]
            }
        ],
        "RequestId": "21120f4e-9073-4c08-af19-0886accbbdac"
    }
}
```

