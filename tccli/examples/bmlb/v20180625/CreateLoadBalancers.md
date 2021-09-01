**Example 1: 创建一个外网负载均衡实例**



Input: 

```
tccli bmlb CreateLoadBalancers --cli-unfold-argument  \
    --GoodsNum 1 \
    --LoadBalancerType open \
    --VpcId vpc-34cxlz7z \
    --IpProtocolType ipv4
```

Output: 
```
{
    "Response": {
        "LoadBalancerIds": [
            "lb-m1i50ynj"
        ],
        "TaskId": "2385670",
        "RequestId": "99e29d13-71a3-4d75-b938-e4241a4f7aa6"
    }
}
```

