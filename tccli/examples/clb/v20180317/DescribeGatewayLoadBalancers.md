**Example 1: 指定实例ID查询网关负载均衡**

指定实例ID查询网关负载均衡

Input: 

```
tccli clb DescribeGatewayLoadBalancers --cli-unfold-argument  \
    --LoadBalancerIds abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LoadBalancerSet": [
            {
                "LoadBalancerId": "abc",
                "LoadBalancerName": "abc",
                "Vips": [
                    "abc"
                ],
                "SubnetId": "abc",
                "Status": 1,
                "InternetMaxBandwidthOut": 0,
                "DeleteProtect": true,
                "TargetGroupId": "abc",
                "VpcId": "abc",
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "Specifications": "abc",
                "CreateTime": "abc",
                "AssociateAclGroup": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

