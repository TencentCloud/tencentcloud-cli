**Example 1: 查询VPC列表**



Input: 

```
tccli vpc DescribeVpcInternal --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2 \
    --Filters.0.Name vpc-id \
    --Filters.0.Values vpc-p5sf61yj \
    --Filters.1.Name vpc-name \
    --Filters.1.Values 测试dhcp
```

Output: 
```
{
    "Response": {
        "VpcSet": [
            {
                "VpcId": "vpc-p5sf61yj",
                "VpcName": "测试dhcp",
                "CidrBlock": "10.0.0.0/16",
                "Ipv6CidrBlock": "3402:4e00:20:1200::/56",
                "IsDefault": false,
                "EnableMulticast": false,
                "CreatedTime": "2018-04-25 10:26:26",
                "EnableDhcp": true,
                "DhcpOptionsId": "dopt-8g7k5qfq",
                "DnsServerSet": [
                    "10.0.0.1",
                    "183.60.82.98"
                ],
                "DomainName": "aa.bb.cc",
                "TagSet": [],
                "AssistantCidrSet": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "6a44afb7-0644-4ff9-9761-3502f99d3a15"
    }
}
```

