**Example 1: 增加主题分区**



Input: 

```
tccli ckafka CreatePartition --cli-unfold-argument  \
    --InstanceId xxx \
    --TopicName xxx \
    --PartitionNum xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok[apply success]"
        },
        "RequestId": "483c3edd-a2ac-420c-905d-47a5ec7de4ad"
    }
}
```

