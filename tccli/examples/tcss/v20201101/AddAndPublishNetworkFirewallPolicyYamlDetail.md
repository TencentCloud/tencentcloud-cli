**Example 1: 容器网络创建yaml网络策略添加任务示例**



Input: 

```
tccli tcss AddAndPublishNetworkFirewallPolicyYamlDetail --cli-unfold-argument  \
    --PolicyName fshduis \
    --Description  \
    --ClusterId cls-hjsdfh \
    --Yaml YXNkZmFzZGZhZHNmYXNkZmFzZGY=
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

