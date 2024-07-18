**Example 1: 创建接口**



Input: 

```
tccli vpc ModifyRouteTableSelectionPolicies --cli-unfold-argument  \
    --CcnId ccn-mnvhfmv9 \
    --SelectionPolicies.0.InstanceType VPC \
    --SelectionPolicies.0.InstanceId vpc-2345rfgt \
    --SelectionPolicies.0.SourceCidrBlock 10.0.0.0/24 \
    --SelectionPolicies.0.RouteTableId ccnrtb-3456trfg
```

Output: 
```
{
    "Response": {
        "RequestId": "ba7c7681-e051-469a-b0fc-210a373490a4"
    }
}
```

