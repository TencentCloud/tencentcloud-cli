**Example 1: 查询VPC列表**

查询VPC列表

Input: 

```
tccli vpc DescribeVpcs --cli-unfold-argument  \
    --Limit 2 \
    --Filters.0.Values 192.168.0.0 10.0.0.0 \
    --Filters.0.Name cidr-block \
    --Filters.1.Values false \
    --Filters.1.Name is-default \
    --Offset 0
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

**Example 2: 查询绑定了标签的VPC列表**

查询绑定了标签键值对（city:shanghai）的vpc。

Input: 

```
tccli vpc DescribeVpcs --cli-unfold-argument  \
    --Limit 2 \
    --Filters.0.Values shanghai \
    --Filters.0.Name tag:city \
    --Offset 0
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
                "EnableDhcp": true,
                "EnableMulticast": false,
                "CreatedTime": "2018-04-25 10:26:26",
                "DhcpOptionsId": "dopt-8g7k5qfq",
                "DnsServerSet": [
                    "10.0.0.1",
                    "183.60.82.98"
                ],
                "TagSet": [
                    {
                        "Key": "city",
                        "Value": "shanghai"
                    }
                ],
                "AssistantCidrSet": [
                    {
                        "CidrBlock": "192.168.1.0/24",
                        "AssistantType": 0,
                        "SubnetSet": []
                    }
                ],
                "DomainName": "aa.bb.cc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "6a44afb7-0644-4ff9-9761-3502f99d3a15"
    }
}
```

