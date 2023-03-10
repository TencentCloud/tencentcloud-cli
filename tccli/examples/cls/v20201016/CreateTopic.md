**Example 1: 创建日志主题**

创建日志主题

Input: 

```
tccli cls CreateTopic --cli-unfold-argument  \
    --LogsetId xxxxxx-xx-xx-xx-xxxxxxxx \
    --TopicName testname \
    --PartitionCount 1 \
    --Period 12
```

Output: 
```
{
    "Response": {
        "TopicId": "xxxx-xx-xx-xx-xxxxxxxx",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

