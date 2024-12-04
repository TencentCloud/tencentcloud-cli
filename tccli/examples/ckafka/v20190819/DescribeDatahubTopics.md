**Example 1: 查询Datahub主题列表**



Input: 

```
tccli ckafka DescribeDatahubTopics --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "136d14bc-109d-4b1a-8b2c-de58cd04536d",
        "Result": {
            "TopicList": [
                {
                    "Name": "1300957330-devin-topic-test",
                    "Note": "",
                    "PartitionNum": 1,
                    "RetentionMs": 86400000,
                    "Status": 1,
                    "TopicId": "topic-elo4dm34",
                    "TopicName": "1300957330-devin-topic-test"
                },
                {
                    "Name": "1300957330-rxtest",
                    "Note": "",
                    "PartitionNum": 1,
                    "RetentionMs": 86400000,
                    "Status": 1,
                    "TopicId": "topic-2kcw8efy",
                    "TopicName": "1300957330-rxtest"
                },
                {
                    "Name": "1300957330-tanxing-qiang-2nd",
                    "Note": "",
                    "PartitionNum": 1,
                    "RetentionMs": 86400000,
                    "Status": 1,
                    "TopicId": "topic-g1ntq6se",
                    "TopicName": "1300957330-tanxing-qiang-2nd"
                },
                {
                    "Name": "1300957330-test",
                    "Note": "",
                    "PartitionNum": 1,
                    "RetentionMs": 86400000,
                    "Status": 1,
                    "TopicId": "topic-4621aeam",
                    "TopicName": "1300957330-test"
                },
                {
                    "Name": "1300957330-test-1",
                    "Note": "",
                    "PartitionNum": 1,
                    "RetentionMs": 86400000,
                    "Status": 1,
                    "TopicId": "topic-houq8qfw",
                    "TopicName": "1300957330-test-1"
                },
                {
                    "Name": "1300957330-test-topic2",
                    "Note": "",
                    "PartitionNum": 2,
                    "RetentionMs": 86400000,
                    "Status": 1,
                    "TopicId": "topic-ar3abkmu",
                    "TopicName": "1300957330-test-topic2"
                },
                {
                    "Name": "1300957330-testttt",
                    "Note": "",
                    "PartitionNum": 1,
                    "RetentionMs": 86400000,
                    "Status": 1,
                    "TopicId": "topic-gdbt9w28",
                    "TopicName": "1300957330-testttt"
                },
                {
                    "Name": "1300957330-topic1",
                    "Note": "",
                    "PartitionNum": 1,
                    "RetentionMs": 86400000,
                    "Status": 1,
                    "TopicId": "topic-ehzi5lue",
                    "TopicName": "1300957330-topic1"
                }
            ],
            "TotalCount": 8
        }
    }
}
```

