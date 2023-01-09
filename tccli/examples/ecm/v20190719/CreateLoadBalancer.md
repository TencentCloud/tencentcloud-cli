**Example 1: 购买负载均衡实例**

购买负载均衡实例

Input: 

```
tccli ecm CreateLoadBalancer --cli-unfold-argument  \
    --VipIsp CUCC \
    --VpcId vpc-12345678 \
    --InternetAccessible.InternetMaxBandwidthOut 2000 \
    --LoadBalancerType OPEN \
    --LoadBalancerName testname \
    --EcmRegion ap-hangzhou-ecm
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

