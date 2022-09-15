**Example 1: 用于查询弹性网卡IPv6地址**



Input: 

```
tccli vpc DescribeEniIpv6Internal --cli-unfold-argument  \
    --WanIp 1.1.1.1 \
    --VpcId 1 \
    --EniId 1 \
    --Description desc \
    --Mac 52:54:00:31:13:96 \
    --PrivateIp 1.1.1.1 \
    --UniqueEniId eniid \
    --State 1 \
    --PublicIpFlag 0 \
    --BlockedFlag 0 \
    --Owner 123123123 \
    --UniqueVpcId vpc-jmaywf6r \
    --Type 1
```

Output: 
```
{
    "Response": {
        "GetEniIPv6Result": [
            {
                "MappedMarkerId": "58.0.0.5",
                "VpcId": 74664,
                "EniId": 28892,
                "UniqueEniId": "eni-poxpxmdf",
                "UniqueVpcId": "vpc-ih5wn2ub",
                "PublicIpFlag": 1,
                "HavIpFlag": 0,
                "Owner": "251005839",
                "Mac": "20:90:6F:4E:4A:D1",
                "PrivateIp": "2402:4e00:1000:7400:0:9028:a2c9:85b2",
                "State": 1,
                "WanIp": "",
                "Type": 0,
                "CreateTime": "2020-03-24 17:27:22",
                "BlockedFlag": 0,
                "Description": ""
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

