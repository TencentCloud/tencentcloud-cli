**Example 1: 多条件过滤查询HAVIP列表**



Input: 

```
tccli ecm DescribeHaVips --cli-unfold-argument  \
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

