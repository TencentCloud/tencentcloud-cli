**Example 1: CreateRejectedQuestion**



Input: 

```
tccli lke CreateRejectedQuestion --cli-unfold-argument  \
    --BotBizId 2078368566271856448 \
    --Question 今天天气怎么样 \
    --BusinessSource 2 \
    --EnableScope 2 \
    --CustomReply.Enabled True \
    --CustomReply.Content 今天晴天
```

Output: 
```
{
    "Response": {
        "RequestId": "f317129b-dca4-4b73-942a-f54678516819"
    }
}
```

