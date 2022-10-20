**Example 1: 容器网络创建检查Yaml网络策略任务示例**



Input: 

```
tccli tcss CheckNetworkFirewallPolicyYaml --cli-unfold-argument  \
    --PolicyName xx \
    --Description xx \
    --ClusterId xx \
    --Yaml xxx
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

