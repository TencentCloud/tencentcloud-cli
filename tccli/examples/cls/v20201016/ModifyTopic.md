**Example 1: 修改日志主题**

修改日志主题

Input: 

```
tccli cls ModifyTopic --cli-unfold-argument  \
    --TopicId 866f8a15-ae8e-4ab4-afb2-4ff169fa3dc0 \
    --TopicName testname \
    --Status False \
    --Period 10
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

