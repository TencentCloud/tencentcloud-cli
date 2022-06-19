**Example 1: 用于从指定 VPC 中申请一个可用 IP**



Input: 

```
tccli vpc ApplyIpInternal --cli-unfold-argument  \
    --IpType 11 \
    --VpcId 1 \
    --UniqueVpcId vpc-xxx \
    --SubnetId 1 \
    --UniqueSubnetId subnet-xxx \
    --ZoneId 1 \
    --Subnet 172.16.0.0 \
    --Mask 255.255.240.0 \
    --Expire 0 \
    --Ip 1.1.1.1 \
    --IntIp 1231231 \
    --UniqueInstanceId ins-xxxx \
    --Owner 2323232
```

Output: 
```
{
    "Response": {
        "IntGateway": 2886729729,
        "Subnet": "172.16.0.0",
        "VpcId": 78257,
        "IntSubnet": 2886729728,
        "UniqueVpcId": "vpc-jmaywf6r",
        "Min": 2886729728,
        "Max": 2886733823,
        "Mask": "255.255.240.0",
        "IntIp": 2886729760,
        "Ip": "172.16.0.32",
        "Gateway": "172.16.0.1",
        "IpType": 0,
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

