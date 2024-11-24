**Example 1: 查询内网保留 IP**

查询内网保留 IP

Input: 

```
tccli vpc DescribeReserveIpAddresses --cli-unfold-argument  \
    --ReserveIpIds rsvip-eaq2f4pc rsvip-2g134x24
```

Output: 
```
{
    "Response": {
        "RequestId": "2d32beeb-0750-4ef9-a2f9-e4e7bbb0ec7f",
        "ReserveIpAddressSet": [
            {
                "CreatedTime": "2024-11-06 12:01:57",
                "Description": "desc_ivan",
                "IpType": 0,
                "Name": "name_ivan",
                "ReserveIpAddress": "10.0.5.99",
                "ReserveIpId": "rsvip-eaq2f4pc",
                "ResourceId": "",
                "State": "UnBind",
                "TagSet": [],
                "VpcId": "vpc-mcqaoy0f"
            },
            {
                "CreatedTime": "2024-11-06 12:01:57",
                "Description": "desc_ivan",
                "IpType": 0,
                "Name": "name_ivan",
                "ReserveIpAddress": "10.0.5.50",
                "ReserveIpId": "rsvip-2g134x24",
                "ResourceId": "",
                "State": "UnBind",
                "TagSet": [],
                "VpcId": "vpc-mcqaoy0f"
            }
        ],
        "TotalCount": 2
    }
}
```

**Example 2: 根据标签过滤查询保留 IP**

根据标签过滤查询保留 IP

Input: 

```
tccli vpc DescribeReserveIpAddresses --cli-unfold-argument  \
    --Filters.0.Name tag-key \
    --Filters.0.Values ivan_reserve_ip
```

Output: 
```
{
    "Response": {
        "RequestId": "e168d943-d647-4c0a-ada4-50a90015ded8",
        "ReserveIpAddressSet": [
            {
                "CreatedTime": "2024-11-06 17:30:06",
                "Description": "desc_ivan",
                "IpType": 0,
                "Name": "name_ivan",
                "ReserveIpAddress": "10.0.5.89",
                "ReserveIpId": "rsvip-du6lo6fu",
                "ResourceId": "",
                "State": "UnBind",
                "TagSet": [
                    {
                        "Key": "ivan_reserve_ip",
                        "Value": "hello"
                    }
                ],
                "VpcId": "vpc-mcqaoy0f"
            }
        ],
        "TotalCount": 1
    }
}
```

