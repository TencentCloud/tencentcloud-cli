**Example 1: 查询结果**



Input: 

```
tccli tcss DescribeNetworkFirewallPodLabelsList --cli-unfold-argument  \
    --ClusterId cls-new \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "a6405e01-bf4f-4044-abe9-4458783a3066",
        "TotalCount": 9,
        "PodList": [
            {
                "PodName": "hello",
                "Namespace": "default",
                "Labels": "new=test"
            }
        ]
    }
}
```

