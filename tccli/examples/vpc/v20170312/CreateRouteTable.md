**Example 1: 创建路由表**

创建路由表

Input: 

```
tccli vpc CreateRouteTable --cli-unfold-argument  \
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
            "LocalCidrForCcn": [
                {
                    "Cidr": "10.1.0.0/24",
                    "PublishedToVbc": true
                }
            ],
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

