**Example 1: 容器网络创建网络策略添加并发布任务示例**



Input: 

```
tccli tcss AddAndPublishNetworkFirewallPolicyDetail --cli-unfold-argument  \
    --PolicyName NewStrategy \
    --CustomPolicy.0.Direction FROM \
    --Description describe content \
    --ClusterId cls-new \
    --FromPolicyRule 1 \
    --Namespace default \
    --ToPolicyRule 2 \
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

