**Example 1: 用于获取根据rs查询规则**



Input: 

```
tccli vpc DescribeServiceByRealServerInternal --cli-unfold-argument  \
    --VpcId 1 \
    --UniqueVpcId vpc-xxx \
    --Vip 1.1.1.1 \
    --VirtualPort 4432 \
    --PrivateIp 1.1.1.1 \
    --PrivatePort 3232
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

