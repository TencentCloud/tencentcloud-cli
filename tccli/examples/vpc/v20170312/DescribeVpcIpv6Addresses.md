**Example 1: 查询VPC内IPv6地址列表**

查询VPC内IPv6地址列表

Input: 

```
tccli vpc DescribeVpcIpv6Addresses --cli-unfold-argument  \
    --VpcId vpc-rkxd3pgh
```

Output: 
```
{
    "Response": {
        "Ipv6AddressSet": [
            {
                "Ipv6Address": "2402:4e00:1000:101:0:8d1a:6c7b:c0e8",
                "Ipv6AddressType": "CVM",
                "CidrBlock": "2402:4e00:1000:101::/64",
                "CreatedTime": "2019-03-01 21:18:07"
            },
            {
                "Ipv6Address": "2402:4e00:1000:101:0:8d20:3e2:683",
                "Ipv6AddressType": "CVM",
                "CidrBlock": "2402:4e00:1000:101::/64",
                "CreatedTime": "2019-03-04 16:00:36"
            },
            {
                "Ipv6Address": "2402:4e00:1000:101:0:8d20:3f5:8b0f",
                "Ipv6AddressType": "CVM",
                "CidrBlock": "2402:4e00:1000:101::/64",
                "CreatedTime": "2019-03-04 16:00:48"
            },
            {
                "Ipv6Address": "2402:4e00:1000:101:0:8d24:30a5:d9f3",
                "Ipv6AddressType": "CVM",
                "CidrBlock": "2402:4e00:1000:101::/64",
                "CreatedTime": "2019-03-06 17:49:05"
            },
            {
                "Ipv6Address": "2402:4e00:1000:101:0:8d2e:133c:e12c",
                "Ipv6AddressType": "CVM",
                "CidrBlock": "2402:4e00:1000:101::/64",
                "CreatedTime": "2019-03-11 15:45:07"
            },
            {
                "Ipv6Address": "2402:4e00:1000:108:0:8d24:690c:59c6",
                "Ipv6AddressType": "CVM",
                "CidrBlock": "2402:4e00:1000:108::/64",
                "CreatedTime": "2019-03-06 20:26:47"
            }
        ],
        "TotalCount": 6,
        "RequestId": "ee464fec-e13e-401b-87f0-f93f047550c2"
    }
}
```

