**Example 1: NAT网关解绑子网**



Input: 

```
tccli bmvpc UnbindSubnetsFromNatGateway --cli-unfold-argument  \
    --NatId nat-1tw1oc0t \
    --VpcId vpc-mi51u7gs \
    --SubnetIds subnet-d3668cur subnet-o9lo3es1
```

Output: 
```
{
    "Response": {
        "TaskId": 18421,
        "RequestId": "cc33a7eb-e3c2-4c04-a9ae-e3872f24ab18"
    }
}
```

