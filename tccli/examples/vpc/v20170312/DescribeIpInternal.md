**Example 1: 用于查询IP地址的详情**



Input: 

```
tccli vpc DescribeIpInternal --cli-unfold-argument  \
    --VpcId 1 \
    --UniqueVpcId vpc-xxx \
    --Ip 1.1.1.1 \
    --Subnet 1.1.1.1 \
    --IpType 1 \
    --Flag 0 \
    --UniqueInstanceId ins-xxx
```

Output: 
```
{
    "Response": {
        "IpSet": [
            {
                "Subnet": "169.254.128.0",
                "VpcId": 78257,
                "DirtyFlag": 0,
                "IntSubnet": 2852028416,
                "UniqueVpcId": "vpc-jmaywf6r",
                "Ip": "169.254.128.2",
                "Mask": "255.255.128.0",
                "Gateway": "169.254.128.1",
                "Flag": 0,
                "UniqueInstanceId": "",
                "IpType": 0,
                "CreateTime": "2021-03-22 21:35:59"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

