**Example 1: 批量设置云产品日志主题LogType**

用于批量设置云产品日志主题LogType

Input: 

```
tccli cls BatchSetCloudProductLogType --cli-unfold-argument  \
    --AssumerName example-assumer \
    --LogType access-log \
    --TopicIds a******u_test_***3
```

Output: 
```
{
    "Response": {
        "RequestId": "ead6751e-1ad8-422c-b606-b2277f10ed6e"
    }
}
```

