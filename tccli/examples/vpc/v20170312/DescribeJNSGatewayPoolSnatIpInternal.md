**Example 1: demo**



Input: 

```
tccli vpc DescribeJNSGatewayPoolSnatIpInternal --cli-unfold-argument  \
    --SubnetId 2007466 \
    --Owner 251197522 \
    --UniqueVpcId vpc-7zayowkt \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "GetJNSGatewayPoolSnatIpResult": [
            {
                "VpcId": 16769060,
                "UniqueVpcId": "vpc-7zayowkt",
                "Owner": "251197522",
                "UniqueSubnetId": "subnet-oqocm8m6",
                "SNATIp": "169.254.128.12",
                "PoolId": 39285,
                "SubnetId": 2007466,
                "GatewayIp": "9.241.203.205",
                "CreateTime": "2022-06-16 19:52:01"
            }
        ],
        "RequestId": "ec37ad59-06c9-490b-97f6-227b62839725"
    }
}
```

