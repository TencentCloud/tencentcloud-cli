**Example 1: 修改 NAT 网关高级属性**

修改 NAT 网关的超时时间

Input: 

```
tccli vpc ModifyNatGatewayAdvancedAttribute --cli-unfold-argument  \
    --NatGatewayId nat-2njz5nh8 \
    --UDPMappingTimeout 180 \
    --TCPEstablishedConnectionTimeout 10800 \
    --TCPTimeWaitTimeout 120
```

Output: 
```
{
    "Response": {
        "RequestId": "34557d2b-28ea-4270-b76b-bf21328157d7"
    }
}
```

