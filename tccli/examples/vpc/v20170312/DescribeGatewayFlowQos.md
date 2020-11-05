**Example 1: Example 1: Querying QoS bandwidth limit of inbound IP flow in a VPN gateway**



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

