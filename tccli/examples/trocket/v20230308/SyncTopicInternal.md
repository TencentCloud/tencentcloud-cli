**Example 1: 同步topic**



Input: 

```
tccli trocket SyncTopicInternal --cli-unfold-argument  \
    --Topic topic-a \
    --InstanceId rocketmq-47x924vjavzz \
    --Perm S_RW_D_R \
    --Namespace def
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "7e4465fd-fc94-4f37-bcd3-f4e858a18a85"
    }
}
```

