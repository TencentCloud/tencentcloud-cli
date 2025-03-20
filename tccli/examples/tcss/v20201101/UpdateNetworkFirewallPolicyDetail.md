**Example 1: 容器网络创建网络策略更新任务示例**



Input: 

```
tccli tcss UpdateNetworkFirewallPolicyDetail --cli-unfold-argument  \
    --Id 22 \
    --CustomPolicy.0.Direction FROM \
    --Description just for develop \
    --ClusterId cls-sdfdsf \
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

