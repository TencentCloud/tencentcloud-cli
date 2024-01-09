**Example 1: 恢复订阅任务**

通过重启尝试恢复一个报错的任务

Input: 

```
tccli dts ResumeSubscribe --cli-unfold-argument  \
    --SubscribeId subs-9jyki7hniw
```

Output: 
```
{
    "Response": {
        "RequestId": "b048a800-f2fe-11ed-a211-5df19a912eab"
    }
}
```

