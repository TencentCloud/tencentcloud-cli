**Example 1: NAT网关解绑EIP**



Input: 

```
tccli bmvpc UnbindEipsFromNatGateway --cli-unfold-argument  \
    --NatId nat-2duawe5v \
    --VpcId vpc-mi51u7gs \
    --AssignedEips 139.199.40.16
```

Output: 
```
{
    "Response": {
        "TaskId": 18417,
        "RequestId": "e16cdd36-43e2-4748-bcf8-56e999953bed"
    }
}
```

