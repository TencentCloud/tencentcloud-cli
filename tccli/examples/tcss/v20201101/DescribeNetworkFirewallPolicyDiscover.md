**Example 1: 容器网络查询网络策略自动发现任务进度示例**



Input: 

```
tccli tcss DescribeNetworkFirewallPolicyDiscover --cli-unfold-argument  \
    --TaskId 34702
```

Output: 
```
{
    "Response": {
        "RequestId": "ed202021-696e-4c03-a726-ca459c47c4ea",
        "TaskStatus": "Task_Succ"
    }
}
```

