**Example 1: 查询任务状态**



Input: 

```
tccli ckafka DescribeTaskStatus --cli-unfold-argument  \
    --FlowId 1003
```

Output: 
```
{
    "Response": {
        "Result": {
            "Status": 0,
            "Output": "success"
        },
        "RequestId": "ca7d6645-e33b-436c-8c83-b2a1229a57fa"
    }
}
```

