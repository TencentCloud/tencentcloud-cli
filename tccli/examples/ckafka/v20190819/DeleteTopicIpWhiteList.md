**Example 1: 删除主题IP白名单**



Input: 

```
tccli ckafka DeleteTopicIpWhiteList --cli-unfold-argument  \
    --InstanceId xxx \
    --TopicName xxxx \
    --IpWhiteList.n xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok[apply success]"
        },
        "RequestId": "b800c966-083a-40f5-8d54-44f40c6b364f"
    }
}
```

