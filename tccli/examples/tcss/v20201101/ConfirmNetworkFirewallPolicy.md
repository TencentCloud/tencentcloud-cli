**Example 1: 容器网络创建网络策略确认任务示例**



Input: 

```
tccli tcss ConfirmNetworkFirewallPolicy --cli-unfold-argument  \
    --ClusterId cls-1324 \
    --Id 1
```

Output: 
```
{
    "Response": {
        "RequestId": "345da107-dfdf-48f0-9796-e6723bdc102e",
        "TaskId": 32501,
        "Result": "Succ"
    }
}
```

