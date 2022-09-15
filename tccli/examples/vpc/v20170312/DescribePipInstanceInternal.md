**Example 1: 用于获取弹性网卡ip绑定的弹性网卡信息和子机信息**



Input: 

```
tccli vpc DescribePipInstanceInternal --cli-unfold-argument  \
    --WanIp 1.1.1.1 \
    --VpcId 1 \
    --EniId 1 \
    --EniType 1 \
    --PrivateIp 1.1.1.1 \
    --UniqueEniId eniid \
    --Mac 255.255.255.255 \
    --Limit 100 \
    --Offset 0 \
    --Owner 123123123 \
    --UniqueVpcId vpc-jmaywf6r \
    --PrivateIpType 1 \
    --UniqueSubnetId subnet-asdasda
```

Output: 
```
{
    "Response": {
        "Total": 12,
        "GetPipInstanceResult": [
            {
                "WanInLimit": 0,
                "VpcId": 81292,
                "EniId": 2225667,
                "UniqueVpcId": "vpc-7f2w7dl7",
                "InstanceId": "",
                "LanInLimit": 0,
                "PrivateIp": "10.0.0.12",
                "Bandwidth": 0,
                "UniqueSubnetId": "subnet-fjfixflc",
                "Owner": "251197522",
                "Uuid": "",
                "LanOutLimit": 0,
                "EniPipId": 40615,
                "State": 1,
                "WanIp": "0.0.0.0",
                "Type": 1,
                "EniType": 0,
                "HavIpFlag": 0,
                "HostIp": "",
                "CreateTime": "2021-04-25 14:45:56",
                "UniqueEniId": "eni-kr5u4sbl",
                "Mac": "20:90:6F:8D:9E:70",
                "DhcpIpFlag": 0,
                "WanOutLimit": 0,
                "BlockedFlag": 0
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

