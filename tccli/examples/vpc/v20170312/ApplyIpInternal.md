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
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

