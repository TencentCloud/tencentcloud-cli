**Example 1: 容器网络更新Yaml网络策略任务示例**



Input: 

```
tccli tcss UpdateNetworkFirewallPolicyYamlDetail --cli-unfold-argument  \
    --Description desc \
    --ClusterId cls-67898 \
    --Id 1 \
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

