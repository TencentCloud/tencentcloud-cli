**Example 1: ModifyRejectedQuestion**



Input: 

```
tccli lke ModifyRejectedQuestion --cli-unfold-argument  \
    --BotBizId 2078368566271856448 \
    --Question 今天天气怎么样？x \
    --RejectedBizId 2092258772108747904 \
    --EnableScope 2 \
    --CustomReply.Enabled True \
    --CustomReply.Content 今天下雨
```

Output: 
```
{
    "Response": {
        "RequestId": "be66a916-01b4-4c95-a221-c09c06bd6d94"
    }
}
```

