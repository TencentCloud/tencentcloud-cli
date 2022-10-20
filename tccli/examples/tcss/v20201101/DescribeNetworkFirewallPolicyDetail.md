**Example 1: 容器网络集群查看策略详情示例**



Input: 

```
tccli tcss DescribeNetworkFirewallPolicyDetail --cli-unfold-argument  \
    --Id 1
```

Output: 
```
{
    "Response": {
        "PolicyName": "xx",
        "CustomPolicy": [
            {
                "Peer": [
                    {
                        "NamespaceSelector": "xx",
                        "PeerType": "xx",
                        "PodSelector": "xx",
                        "IPBlock": "xx"
                    }
                ],
                "Direction": "xx",
                "Ports": [
                    {
                        "Protocol": "xx",
                        "Port": "xx"
                    }
                ]
            }
        ],
        "Description": "xx",
        "ClusterId": "xx",
        "FromPolicyRule": 0,
        "PublishResult": "xx",
        "Namespace": "xx",
        "NetworkPolicyPlugin": "xx",
        "PodSelector": "xx",
        "PublishStatus": "xx",
        "ToPolicyRule": 0,
        "RequestId": "xx",
        "PolicyCreateTime": "xx",
        "PolicySourceType": "xx"
    }
}
```

