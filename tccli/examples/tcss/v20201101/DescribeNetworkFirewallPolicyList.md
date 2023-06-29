**Example 1: 查询结果**



Input: 

```
tccli tcss DescribeNetworkFirewallPolicyList --cli-unfold-argument  \
    --ClusterId cls-ee \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "a6405e01-bf4f-4044-abe9-4458783a3066",
        "TotalCount": 9,
        "NetPolicy": [
            {
                "PolicySourceType": "xx",
                "FromPolicyRule": 0,
                "PublishResult": "xx",
                "Namespace": "xx",
                "NetworkPolicyPlugin": "xx",
                "PolicyCreateTime": "xx",
                "PublishStatus": "xx",
                "ToPolicyRule": 0,
                "PodSelector": "xx",
                "Description": "xx",
                "Id": 1,
                "Name": "xx"
            }
        ]
    }
}
```

**Example 2: 策略列表**



Input: 

```
tccli tcss DescribeNetworkFirewallPolicyList --cli-unfold-argument  \
    --ClusterId cls-o9mfjg0i
```

Output: 
```
{
    "Response": {
        "RequestId": "0f209045-f906-4ba4-9f61-105b73ecfcc6",
        "TotalCount": 0,
        "NetPolicy": [
            {
                "Id": 1,
                "Name": "backend-ingress-deny",
                "Description": "",
                "PolicySourceType": "System",
                "PodSelector": "new=roopingliu",
                "Namespace": "default",
                "FromPolicyRule": 0,
                "ToPolicyRule": 0,
                "NetworkPolicyPlugin": "KubeRouter",
                "PublishStatus": "PublishedNoConfirm",
                "PublishResult": "",
                "PolicyCreateTime": "2022-05-10 03:04:34"
            },
            {
                "Id": 8,
                "Name": "policy_test_add",
                "Description": "",
                "PolicySourceType": "Manual",
                "PodSelector": "good=labeld",
                "Namespace": "default",
                "FromPolicyRule": 3,
                "ToPolicyRule": 0,
                "NetworkPolicyPlugin": "KubeRouter",
                "PublishStatus": "unPublishEdit",
                "PublishResult": "",
                "PolicyCreateTime": "2022-06-23 05:40:13"
            },
            {
                "Id": 2,
                "Name": "test-network-policy",
                "Description": "",
                "PolicySourceType": "System",
                "PodSelector": "role=db",
                "Namespace": "default",
                "FromPolicyRule": 0,
                "ToPolicyRule": 0,
                "NetworkPolicyPlugin": "KubeRouter",
                "PublishStatus": "PublishedNoConfirm",
                "PublishResult": "",
                "PolicyCreateTime": "2022-06-13 08:33:35"
            }
        ]
    }
}
```

