**Example 1: 创建路由表**



Input: 

```
tccli ecm CreateRouteTable --cli-unfold-argument  \
    --RouteTableName 测试路由表 \
    --VpcId vpc-loibq08z \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "RouteTable": {
            "VpcId": "vpc-loibq08z",
            "RouteTableId": "rtb-dqbbc9zc",
            "RouteTableName": "测试路由表",
            "AssociationSet": [],
            "RouteSet": [],
            "Main": false,
            "CreatedTime": "0000-00-00 00:00:00"
        },
        "RequestId": "4673c0fc-cb3a-435f-99a7-61a139a31ae4"
    }
}
```

