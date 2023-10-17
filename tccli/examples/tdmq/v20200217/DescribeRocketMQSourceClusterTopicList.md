**Example 1: 查询源集群主题列表**

查询源集群主题列表

Input: 

```
tccli tdmq DescribeRocketMQSourceClusterTopicList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --TaskId 700000780519-o4n3m5g97wgr-3391d15d
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "fba29035-5771-45ee-b4d3-f0e45d6f9e5c",
        "Topics": [
            {
                "Imported": false,
                "Namespace": "tdmq_default",
                "Partitions": 1,
                "Remark": "",
                "TopicName": "broker-a",
                "Type": "Normal"
            },
            {
                "Imported": false,
                "Namespace": "tdmq_default",
                "Partitions": 16,
                "Remark": "",
                "TopicName": "DefaultCluster",
                "Type": "Normal"
            },
            {
                "Imported": false,
                "Namespace": "tdmq_default",
                "Partitions": 1,
                "Remark": "",
                "TopicName": "DefaultCluster_REPLY_TOPIC",
                "Type": "Normal"
            },
            {
                "Imported": false,
                "Namespace": "tdmq_default",
                "Partitions": 8,
                "Remark": "",
                "TopicName": "TopicTest",
                "Type": "Normal"
            },
            {
                "Imported": false,
                "Namespace": "tdmq_default",
                "Partitions": 8,
                "Remark": "",
                "TopicName": "Topic_1018",
                "Type": "Normal"
            },
            {
                "Imported": false,
                "Namespace": "tdmq_default",
                "Partitions": 8,
                "Remark": "",
                "TopicName": "Topic_10240",
                "Type": "Normal"
            },
            {
                "Imported": false,
                "Namespace": "tdmq_default",
                "Partitions": 8,
                "Remark": "",
                "TopicName": "Topic_10388",
                "Type": "Normal"
            },
            {
                "Imported": false,
                "Namespace": "tdmq_default",
                "Partitions": 8,
                "Remark": "",
                "TopicName": "Topic_10722",
                "Type": "Normal"
            },
            {
                "Imported": false,
                "Namespace": "tdmq_default",
                "Partitions": 8,
                "Remark": "",
                "TopicName": "Topic_11334",
                "Type": "Normal"
            },
            {
                "Imported": false,
                "Namespace": "tdmq_default",
                "Partitions": 8,
                "Remark": "",
                "TopicName": "Topic_12187",
                "Type": "Normal"
            }
        ],
        "TotalCount": 54
    }
}
```

**Example 2: 正常调用**

正常调用

Input: 

```
tccli tdmq DescribeRocketMQSourceClusterTopicList --cli-unfold-argument  \
    --Limit 2 \
    --Offset 0 \
    --TaskId 700000780521-migratetest-d93e34d2
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "2445d687-10f2-403a-a46a-cfa9a939074f",
        "Topics": [
            {
                "Imported": false,
                "Namespace": "",
                "Partitions": 1,
                "Remark": null,
                "TopicName": "OFFSET_MOVED_EVENT",
                "Type": null
            },
            {
                "Imported": false,
                "Namespace": "",
                "Partitions": 8,
                "Remark": null,
                "TopicName": "Topic_213",
                "Type": null
            }
        ],
        "TotalCount": 2
    }
}
```

