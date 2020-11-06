**Example 1: Creating a route table**



Input: 

```
tccli vpc CreateRouteTable --cli-unfold-argument  \
    --Version 2017-03-12 \
    --RouteTableName TestRouteTable \
    --VpcId vpc-2at5y1pn \
    --Tags.0.Key city \
    --Tags.0.Value shanghai
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "RouteTable": {
            "RouteTableId": "rtb-azd4dt1c",
            "VpcId": "vpc-2at5y1pn",
            "RouteTableName": "TestRouteTable",
            "AssociationSet": [],
            "RouteSet": [],
            "Main": false,
            "TagSet": [
                {
                    "Key": "city",
                    "Value": "shanghai"
                }
            ]
        }
    }
}
```

