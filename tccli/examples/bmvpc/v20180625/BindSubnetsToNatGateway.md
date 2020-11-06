**Example 1: NAT网关绑定子网**



Input: 

```
tccli bmvpc BindSubnetsToNatGateway --cli-unfold-argument  \
    --NatId nat-1tw1oc0t \
    --VpcId vpc-mi51u7gs \
    --SubnetIds subnet-d3668cur subnet-o9lo3es1
```

Output: 
```
{
    "Response": {
        "TaskId": 18419,
        "RequestId": "28260e47-0047-4f9a-9d2d-405053e284ac"
    }
}
```

