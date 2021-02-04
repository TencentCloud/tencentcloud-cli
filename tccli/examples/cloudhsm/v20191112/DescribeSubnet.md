**Example 1: 查询子网列表**

查询子网列表

Input: 

```
tccli cloudhsm DescribeSubnet --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --VpcId vpc-2at5y1pn
```

Output: 
```
{
    "Response": {
        "SubnetList": [
            {
                "VpcId": "vpc-2at5y1pn",
                "SubnetId": "subnet-otu92seu",
                "SubnetName": "默认广州二区子网",
                "CidrBlock": "172.16.16.0/24",
                "Ipv6CidrBlock": "3402:4e00:20:1201::/64",
                "AvailableIpAddressCount": 2,
                "CreatedTime": "2017-04-20 11:30:48",
                "TotalIpAddressCount": 254,
                "IsDefault": false
            }
        ],
        "TotalCount": 1,
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

