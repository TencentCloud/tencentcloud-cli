**Example 1: 用于退还 VPC IP**



Input: 

```
tccli vpc ReturnIpInternal --cli-unfold-argument  \
    --Owner 121212 \
    --VpcId 1 \
    --UniqueVpcId vpc-xxx \
    --Ip Ip \
    --UniqueInstanceId ins-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

