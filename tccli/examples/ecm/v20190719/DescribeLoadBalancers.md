**Example 1: 查询负载均衡实例列表**



Input: 

```
tccli ecm DescribeLoadBalancers --cli-unfold-argument  \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "RequestId": "8d42288f-3fad-473a-93e6-cab5b219af8e",
        "LoadBalancerSet": [
            {
                "Status": 1,
                "StatusTime": "2020-07-28 10:58:08",
                "VpcId": "vpc-pugaiwf9",
                "LoadBalancerVips": [
                    "101.67.8.110"
                ],
                "VipIsp": "CUCC",
                "CreateTime": "2020-07-28 10:58:06",
                "LoadBalancerId": "lb-a8q643wj",
                "LoadBalancerName": "test",
                "LoadBalancerType": "OPEN",
                "Tags": [
                    {
                        "TagValue": "test",
                        "TagKey": "test"
                    }
                ],
                "NetworkAttributes": {
                    "InternetMaxBandwidthOut": 100
                }
            }
        ],
        "TotalCount": 1
    }
}
```

