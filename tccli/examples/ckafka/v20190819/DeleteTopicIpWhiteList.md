**Example 1: Deleting topic IP whitelist**



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

