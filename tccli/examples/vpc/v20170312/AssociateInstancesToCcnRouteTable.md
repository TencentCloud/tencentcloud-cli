**Example 1: 关联实例到路由表**

关联实例到路由表

Input: 

```
tccli vpc AssociateInstancesToCcnRouteTable --cli-unfold-argument  \
    --CcnId ccn-gree226l \
    --RouteTableId ccnrt-gree2262 \
    --Instances.0.InstanceType VPC \
    --Instances.0.InstanceId vpc-3dr1zrr9
```

Output: 
```
{
    "Response": {
        "RequestId": "627c2362-890f-4f9e-9158-5e457b80d48b"
    }
}
```

