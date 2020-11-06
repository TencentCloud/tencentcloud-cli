**Example 1: Querying CLB instance details**



Input: 

```
tccli clb DescribeLoadBalancersDetail --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
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

