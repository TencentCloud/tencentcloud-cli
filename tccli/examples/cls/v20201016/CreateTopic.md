**Example 1: 创建日志主题**

创建日志主题

Input: 

```
tccli cls CreateTopic --cli-unfold-argument  \
    --LogsetId 29ccb4c0-ab2f-47ab-9dcd-31413b057812 \
    --TopicName testname \
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

**Example 2: 创建指标主题**

创建指标主题

Input: 

```
tccli cls CreateTopic --cli-unfold-argument  \
    --LogsetId 29ccb4c0-ab2f-47ab-9dcd-31413b057812 \
    --TopicName testname \
    --BizType 1 \
    --Period 12
```

Output: 
```
{
    "Response": {
        "TopicId": "6d069a26-1606-4142-9fa6-17ccee4f9bc9",
        "RequestId": "c1731e60-e00d-45ee-a9e8-5343d4f38325"
    }
}
```

