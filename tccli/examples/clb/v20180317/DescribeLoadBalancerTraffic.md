**Example 1: 查询账号下高流量负载均衡**

查询账号下高流量负载均衡

Input: 

```
tccli clb DescribeLoadBalancerTraffic --cli-unfold-argument  \
    --LoadBalancerRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "LoadBalancerTraffic": [
            {
                "LoadBalancerId": "lb-xxxxxx",
                "LoadBalancerName": "lb-name1",
                "Region": "ap-guangzhou",
                "Vip": "1.1.1.1",
                "OutBandwidth": 177.083
            },
            {
                "LoadBalancerId": "lb-kxyz2",
                "LoadBalancerName": "lb-xyzname",
                "Region": "ap-guangzhou",
                "Vip": "2.2.2.2",
                "OutBandwidth": 77.449
            }
        ],
        "RequestId": "03b18184-caf1-40d7-b01a-100010030712"
    }
}
```

