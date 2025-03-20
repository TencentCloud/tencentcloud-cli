**Example 1: 容器网络创建网络策略发布任务示例**



Input: 

```
tccli tcss CreateNetworkFirewallPublish --cli-unfold-argument  \
    --ClusterId cls-sdhfisdf \
    --Id 1002
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

