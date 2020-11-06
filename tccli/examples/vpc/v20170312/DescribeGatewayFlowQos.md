**Example 1: 示例1 查询VPN网关来访IP流控带宽**



Input: 

```
tccli vpc DescribeGatewayFlowQos --cli-unfold-argument  \
    --GatewayId vpngw-4je9dgin
```

Output: 
```
{
    "Response": {
        "GatewayQosSet": [
            {
                "VpcId": "vpc-mrzkofih",
                "IpAddress": "10.0.0.12",
                "Bandwidth": 10,
                "CreateTime": "2020-01-01 10:00:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "5cf1a813-d4f8-4e0c-8f90-c155a84a3ea1"
    }
}
```

