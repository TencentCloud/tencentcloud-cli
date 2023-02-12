**Example 1: 查询负载均衡详细信息**



Input: 

```
tccli clb DescribeLoadBalancersDetail --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "LoadBalancerDetailSet": [],
        "RequestId": "d09b91ba-a81e-4ca3-b423-c64e60127c64"
    }
}
```

