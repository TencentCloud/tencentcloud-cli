**Example 1: 容器网络创建网络策略撤销任务示例**



Input: 

```
tccli tcss CreateNetworkFirewallUndoPublish --cli-unfold-argument  \
    --ClusterId test-clusterid \
    --Id 1021
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

