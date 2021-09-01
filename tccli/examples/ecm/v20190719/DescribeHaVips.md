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
                "VpcId": "vpc-11111111",
                "SubnetId": "subnet-11111111",
                "NetworkInterfaceId": "eni-7tqc2xgl",
                "InstanceId": "ein-1kb08tq6",
                "AddressIp": "",
                "State": "AVAILABLE",
                "Business": "",
                "CreatedTime": "2020-04-03 20:00:05"
            },
            {
                "HaVipId": "havip-bk4275i0",
                "HaVipName": "22",
                "Vip": "10.2.0.14",
                "VpcId": "vpc-22222222",
                "SubnetId": "subnet-22222222",
                "NetworkInterfaceId": "",
                "InstanceId": "",
                "AddressIp": "",
                "Business": "",
                "State": "UNBIND",
                "CreatedTime": "2020-04-03 20:05:33"
            }
        ],
        "TotalCount": 2,
        "RequestId": "1c827bf1-837f-4302-b51a-4d538b7ad249"
    }
}
```

