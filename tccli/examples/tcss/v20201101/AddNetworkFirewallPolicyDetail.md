**Example 1: 容器网络创建网络策略添加任务示例**



Input: 

```
tccli tcss AddNetworkFirewallPolicyDetail --cli-unfold-argument  \
    --PolicyName test-2 \
    --CustomPolicy.0.Direction FROM \
    --Description description1 \
    --ClusterId cls-fsdfw \
    --FromPolicyRule 0 \
    --Namespace default \
    --ToPolicyRule 0 \
    --PodSelector a=b
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

