**Example 1: 创建主题IP白名单**



Input: 

```
tccli ckafka CreateTopicIpWhiteList --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --TopicName topic-name \
    --IpWhiteList 1.1.1.1 10.3.3.4
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok[apply success]",
            "Data": {
                "FlowId": 0
            }
        },
        "RequestId": "b800c966-083a-40f5-8d54-44f40c6b364f"
    }
}
```

