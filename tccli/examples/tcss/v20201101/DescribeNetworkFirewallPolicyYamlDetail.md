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
        "PolicyName": "xx",
        "PolicySourceType": "xx",
        "NetworkPolicyPlugin": "xx",
        "PublishResult": "xx",
        "ClusterId": "xx",
        "Yaml": "xx",
        "PublishStatus": "xx",
        "RequestId": "xx",
        "PolicyCreateTime": "xx",
        "Description": "xx"
    }
}
```

