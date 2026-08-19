**Example 1: 示例**



Input: 

```
tccli csip DescribeEdrExcludeNetworkSegments --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DefaultNetworkSegments": [
            {
                "Desc": "运营商级NAT",
                "Segment": "100.64.0.0/10"
            }
        ],
        "IsModified": true,
        "NetworkSegments": [],
        "TotalCount": 0,
        "RequestId": "412955a7-6426-43fa-879c-520837a00687"
    }
}
```

