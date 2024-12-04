**Example 1: 增加主题分区**



Input: 

```
tccli ckafka CreatePartition --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --TopicName mytopic \
    --PartitionNum 3
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok[apply success]",
            "Data": null
        },
        "RequestId": "483c3edd-a2ac-420c-905d-47a5ec7de4ad"
    }
}
```

