**Example 1: Creating topic IP whitelist**



Input: 

```
tccli ckafka CreateTopicIpWhiteList --cli-unfold-argument  \
    --InstanceId xxxx \
    --TopicName xxx \
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
        "RequestId": "7a6f7927-a435-4e55-8687-f24a8838f744"
    }
}
```

