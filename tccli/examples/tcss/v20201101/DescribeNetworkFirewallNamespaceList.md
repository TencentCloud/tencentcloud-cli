**Example 1: 查询结果**



Input: 

```
tccli tcss DescribeNetworkFirewallNamespaceList --cli-unfold-argument  \
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
        "ClusterNamespaceList": [
            {
                "Name": "hello",
                "Labels": "new=value"
            }
        ]
    }
}
```

**Example 2: 命名空间列表**



Input: 

```
tccli tcss DescribeNetworkFirewallNamespaceList --cli-unfold-argument  \
    --ClusterId cls-o9mfjg0i
```

Output: 
```
{
    "Response": {
        "RequestId": "dee2fbd3-3114-4b17-9cf7-5c456cd703b1",
        "TotalCount": 14,
        "ClusterNamespaceList": [
            {
                "Labels": "key=value",
                "Name": "app-team1"
            }
        ]
    }
}
```

