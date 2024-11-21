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
        "PolicyName": "test",
        "CustomPolicy": [
            {
                "Peer": [
                    {
                        "NamespaceSelector": "default",
                        "PeerType": "",
                        "PodSelector": "",
                        "IPBlock": ""
                    }
                ],
                "Direction": "FROM",
                "Ports": [
                    {
                        "Protocol": "tcp",
                        "Port": "80"
                    }
                ]
            }
        ],
        "Description": "",
        "ClusterId": "cls-dsfhuisdhfis",
        "FromPolicyRule": 0,
        "PublishResult": "",
        "Namespace": "default",
        "NetworkPolicyPlugin": "",
        "PodSelector": "a=b",
        "PublishStatus": "running",
        "ToPolicyRule": 0,
        "RequestId": "392f05bd-bf86-4911-8cf9-b8c2ac0f62ab",
        "PolicyCreateTime": "2024-10-30 12:27:01",
        "PolicySourceType": ""
    }
}
```

