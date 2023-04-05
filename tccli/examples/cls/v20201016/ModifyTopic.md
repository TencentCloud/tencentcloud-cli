**Example 1: 修改日志主题**

修改日志主题

Input: 

```
tccli cls ModifyTopic --cli-unfold-argument  \
    --TopicId xxxxxx-xx-xx-xx-xxxxxxxx \
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

