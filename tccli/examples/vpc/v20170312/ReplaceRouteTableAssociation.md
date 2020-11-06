**Example 1: Replacing the association relation of a route table**



Input: 

```
tccli vpc ReplaceRouteTableAssociation --cli-unfold-argument  \
    --Version 2017-03-12 \
    --RouteTableId rtb-n0yejvje \
    --SubnetId subnet-q2079ils
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

