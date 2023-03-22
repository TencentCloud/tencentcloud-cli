**Example 1: 查询网关负载均衡**

查询网关负载均衡

Input: 

```
tccli clb DescribeGatewayLoadBalancers --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LoadBalancerSet": [
            {
                "Status": 1,
                "TargetGroupId": "xx",
                "VpcId": "xx",
                "Vips": [
                    "x.x.x.x"
                ],
                "Tags": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "Specifications": "xx",
                "ProjectId": 1,
                "DeleteProtect": true,
                "InternetMaxBandwidthOut": 0,
                "LoadBalancerId": "xx",
                "SubnetId": "xx",
                "LoadBalancerName": "xx",
                "CreateTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

