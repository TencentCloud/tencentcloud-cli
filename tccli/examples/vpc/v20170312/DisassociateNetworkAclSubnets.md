**Example 1: Disassociating a network ACL from subnets**



Input: 

```
tccli vpc DisassociateNetworkAclSubnets --cli-unfold-argument  \
    --Version 2017-03-12 \
    --NetworkAclId acl-12345678 \
    --SubnetIds subnet-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

