**Example 1: 按ID过滤查询HAVIP列表**

按ID过滤查询HAVIP列表

Input: 

```
tccli vpc DescribeHaVips --cli-unfold-argument  \
    --HaVipIds havip-bk4275i0 havip-2kce8v4q
```

Output: 
```
{
    "Response": {
        "HaVipSet": [
            {
                "HaVipId": "havip-2kce8v4q",
                "HaVipName": "tadfafd",
                "Vip": "10.3.3.15",
                "VpcId": "vpc-o31qeah3",
                "SubnetId": "subnet-8qywqc4y",
                "NetworkInterfaceId": "",
                "InstanceId": "",
                "AddressIp": "",
                "Business": "",
                "State": "UNBOUND",
                "CreatedTime": "2018-04-03 20:00:05"
            },
            {
                "HaVipId": "havip-bk4275i0",
                "HaVipName": "22",
                "Vip": "10.2.0.14",
                "VpcId": "vpc-2mcdauzl",
                "SubnetId": "subnet-mnmm19fg",
                "NetworkInterfaceId": "",
                "InstanceId": "",
                "AddressIp": "",
                "Business": "",
                "State": "UNBOUND",
                "CreatedTime": "2018-04-03 20:05:33"
            }
        ],
        "TotalCount": 2,
        "RequestId": "1c827bf1-837f-4302-b51a-4d538b7ad249"
    }
}
```

**Example 2: 多条件过滤查询HAVIP列表**

多条件过滤查询HAVIP列表

Input: 

```
tccli vpc DescribeHaVips --cli-unfold-argument  \
    --Filters.0.Name havip-name \
    --Filters.0.Values test \
    --Filters.1.Name vpc-id \
    --Filters.1.Values vpc-6v2ht8q5
```

Output: 
```
{
    "Response": {
        "HaVipSet": [
            {
                "HaVipId": "havip-iyy1ykky",
                "HaVipName": "test modify",
                "Vip": "10.4.6.17",
                "VpcId": "vpc-6v2ht8q5",
                "SubnetId": "subnet-qq51iwr4",
                "NetworkInterfaceId": "",
                "InstanceId": "",
                "AddressIp": "",
                "Business": "",
                "State": "UNBOUND",
                "CreatedTime": "2018-10-09 18:08:16"
            }
        ],
        "TotalCount": 1,
        "RequestId": "659cd6a3-a75a-473c-8280-af27c33da8bd"
    }
}
```

