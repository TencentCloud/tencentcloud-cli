**Example 1: 容器网络查询网络策略策略执行状态示例**



Input: 

```
tccli tcss DescribeNetworkFirewallPolicyStatus --cli-unfold-argument  \
    --TaskId 34702
```

Output: 
```
{
    "Response": {
        "RequestId": "ed202021-696e-4c03-a726-ca459c47c4ea",
        "TaskResult": [
            "xx"
        ],
        "TaskStatus": "Task_Succ"
    }
}
```

