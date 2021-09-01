**Example 1: 更新机器人任务作业状态**



Input: 

```
tccli cr ChangeBotCallStatus --cli-unfold-argument  \
    --Status xx \
    --CallId xx \
    --BotId xx \
    --Module xx \
    --BizDate 2020-09-22 \
    --Operation xx \
    --BotName xx
```

Output: 
```
{
    "Response": {
        "RequestId": "12345-6789-test-from-rest4api"
    }
}
```

