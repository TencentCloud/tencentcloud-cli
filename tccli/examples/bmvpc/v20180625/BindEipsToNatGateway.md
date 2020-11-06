**Example 1: NAT网关绑定已申请的EIP**



Input: 

```
tccli bmvpc BindEipsToNatGateway --cli-unfold-argument  \
    --NatId nat-2duawe5v \
    --VpcId vpc-mi51u7gs \
    --AssignedEips 139.199.40.16
```

Output: 
```
{
    "Response": {
        "TaskId": 18413,
        "RequestId": "a63cf9af-5529-459e-93b8-8f45e38b5770"
    }
}
```

**Example 2: NAT网关绑定新建EIP**



Input: 

```
tccli bmvpc BindEipsToNatGateway --cli-unfold-argument  \
    --NatId nat-2duawe5v \
    --VpcId vpc-mi51u7gs \
    --AutoAllocEipNum 1
```

Output: 
```
{
    "Response": {
        "TaskId": 18415,
        "RequestId": "cb2be9db-6ab7-4fd6-a1c1-935bf78dd8f3"
    }
}
```

