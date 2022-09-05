**Example 1: 获取负载均衡闲置实例**



Input: 

```
tccli clb DescribeIdleLoadBalancers --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 46,
        "IdleLoadBalancers": [
            {
                "LoadBalancerId": "lb-1l1i6a3k",
                "LoadBalancerName": "lb-613054ce",
                "Region": "ap-guangzhou",
                "Vip": "172.16.32.29",
                "IdleReason": "NO_RULES",
                "Status": 1,
                "Forward": 1
            }
        ],
        "RequestId": "afa28690-f148-483f-9727-58c2f1da3794"
    }
}
```

