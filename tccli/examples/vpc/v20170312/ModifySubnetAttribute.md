**Example 1: 修改子网属性**



Input: 

```
tccli vpc ModifySubnetAttribute --cli-unfold-argument  \
    --Version 2017-03-12 \
    --SubnetId subnet-test1234 \
    --SubnetName NewSubnetName \
    --EnableBroadcast true
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

