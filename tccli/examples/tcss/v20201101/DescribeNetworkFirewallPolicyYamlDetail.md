**Example 1: 容器网络集群查看Yaml网络策略详情示例**



Input: 

```
tccli tcss DescribeNetworkFirewallPolicyYamlDetail --cli-unfold-argument  \
    --Id 1
```

Output: 
```
{
    "Response": {
        "PolicyName": "name1",
        "PolicySourceType": "System",
        "NetworkPolicyPlugin": "KubeRouter",
        "PublishResult": "success",
        "ClusterId": "cls-jvrv0kf2",
        "Yaml": "YXNkZmFzZGZhZHNmYXNkZmFzZGY=",
        "PublishStatus": "PublishedNoConfirm",
        "RequestId": "965c55c5-8ab1-4e32-8425-4c44acb5edec",
        "PolicyCreateTime": "2024-10-30 14:35:57",
        "Description": "desc content"
    }
}
```

