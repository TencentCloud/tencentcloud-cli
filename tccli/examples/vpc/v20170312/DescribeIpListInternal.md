**Example 1: demo**



Input: 

```
tccli vpc DescribeIpListInternal --cli-unfold-argument  \
    --Ip 10.4.128.11 \
    --UniqueVpcId vpc-7zayowkt
```

Output: 
```
{
    "Response": {
        "IpSet": [
            {
                "Subnet": "10.4.128.0",
                "VpcId": 16769060,
                "DirtyFlag": 0,
                "IntSubnet": 168067072,
                "UniqueVpcId": "vpc-7zayowkt",
                "Ip": "10.4.128.11",
                "Mask": "255.255.128.0",
                "Gateway": "10.4.128.1",
                "Flag": 1,
                "UniqueInstanceId": "",
                "IpType": 2,
                "CreateTime": "2021-08-27 15:24:27"
            }
        ],
        "RequestId": "c435f01f-1bf9-4e6c-93eb-aa1c1d61481a"
    }
}
```

