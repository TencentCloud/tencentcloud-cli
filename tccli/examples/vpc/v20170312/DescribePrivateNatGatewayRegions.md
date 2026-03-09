**Example 1: 查询私网NAT网关可支持地域**



Input: 

```
tccli vpc DescribePrivateNatGatewayRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RegionSet": [
            {
                "Region": "ap-chongqing"
            },
            {
                "Region": "ap-guangzhou"
            },
            {
                "Region": "ap-shanghai"
            },
            {
                "Region": "ap-beijing"
            },
            {
                "Region": "ap-chengdu"
            }
        ],
        "TotalCount": 5,
        "RequestId": "5f24dd8e-bb8d-4e32-aba5-31a368745c7e"
    }
}
```

