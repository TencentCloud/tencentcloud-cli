**Example 1: 创建日志主题**

创建日志主题

Input: 

```
tccli cls CreateTopic --cli-unfold-argument  \
    --LogsetId 29ccb4c0-ab2f-47ab-9dcd-31413b057812 \
    --TopicName testname \
    --PartitionCount 1 \
    --Period 12
```

Output: 
```
{
    "Response": {
        "TopicId": "866f8a15-ae8e-4ab4-afb2-4ff169fa3dc0",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

