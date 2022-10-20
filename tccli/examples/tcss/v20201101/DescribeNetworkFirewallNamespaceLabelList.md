**Example 1: 查询集群网络空间标签列表示例**



Input: 

```
tccli tcss DescribeNetworkFirewallNamespaceLabelList --cli-unfold-argument  \
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
        "ClusterNamespaceLabelList": [
            {
                "Name": "hello",
                "Labels": "new=test"
            }
        ]
    }
}
```

