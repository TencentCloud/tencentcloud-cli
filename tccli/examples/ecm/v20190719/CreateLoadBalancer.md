**Example 1: 购买负载均衡实例**



Input: 

```
tccli ecm CreateLoadBalancer --cli-unfold-argument  \
    --EcmRegion ap-hangzhou-ecm\
    --VpcId vpc-12345678\
    --LoadBalancerType OPEN\
    --LoadBalancerName testname\
    --VipIsp CUCC\
    --InternetAccessible.InternetMaxBandwidthOut 2000
```

Output: 
```
{
    "Response": {
        "LoadBalancerIds": [
            "lb-mov2697v"
        ],
        "RequestId": "88487432-ee86-4e5d-861b-774374123f89"
    }
}
```

