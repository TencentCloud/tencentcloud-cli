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
                "TargetGroupId": "",
                "VpcId": "vpc-rdiw0xxx",
                "Vips": [
                    "10.0.0.1"
                ],
                "CreateTime": "2024-11-26 16:40:42",
                "Tags": [],
                "DeleteProtect": false,
                "ChargeType": "POSTPAID_BY_HOUR",
                "Isolation": 0,
                "IsolatedTime": ""
            }
        ],
        "RequestId": "7c28eba2-f0d0-427e-9bc2-f44c035825b5"
    }
}
```

**Example 2: 指定标签查询网关负载均衡**

指定标签查询网关负载均衡

Input: 

```
tccli gwlb DescribeGatewayLoadBalancers --cli-unfold-argument  \
    --Filters.0.Name tag:标签键 \
    --Filters.0.Values tag-value
```

Output: 
```
{
    "Response": {
        "LoadBalancerSet": [
            {
                "ChargeType": "POSTPAID_BY_HOUR",
                "CreateTime": "2025-03-15 18:17:37",
                "DeleteProtect": false,
                "IsolatedTime": "",
                "Isolation": 0,
                "LoadBalancerId": "gwlb-jucncd66",
                "LoadBalancerName": "gwlb-jucncd66",
                "OperateProtect": true,
                "Status": 1,
                "SubnetId": "subnet-8yvowms4",
                "Tags": [
                    {
                        "TagKey": "标签键",
                        "TagValue": "tag-value"
                    }
                ],
                "TargetGroupId": "",
                "Vips": [
                    "192.168.192.3"
                ],
                "VpcId": "vpc-ga4sg745"
            }
        ],
        "RequestId": "cfb0e685-2eb7-40c6-9871-91a5a05e946e",
        "TotalCount": 1
    }
}
```

