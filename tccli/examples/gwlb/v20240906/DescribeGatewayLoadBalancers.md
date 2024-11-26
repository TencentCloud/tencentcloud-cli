**Example 1: 指定实例ID查询网关负载均衡**

指定实例ID查询网关负载均衡

Input: 

```
tccli gwlb DescribeGatewayLoadBalancers --cli-unfold-argument  \
    --LoadBalancerIds gwlb-9cpkxxxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LoadBalancerSet": [
            {
                "LoadBalancerId": "gwlb-9cpkxxxx",
                "LoadBalancerName": "the_name_of_gwlb",
                "Status": 1,
                "SubnetId": "subnet-gbi70xxx",
                "TargetGroupId": null,
                "VpcId": "vpc-rdiw0xxx",
                "Vips": [
                    "10.0.0.1"
                ],
                "CreateTime": "2024-11-26 16:40:42",
                "Tags": null,
                "DeleteProtect": false,
                "ChargeType": "POSTPAID_BY_HOUR",
                "Isolation": 0,
                "IsolatedTime": null
            }
        ],
        "RequestId": "7c28eba2-f0d0-427e-9bc2-f44c035825b5"
    }
}
```

