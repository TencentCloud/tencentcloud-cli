**Example 1: 查询NAT边界防火墙开关列表**



Input: 

```
tccli cfw DescribeNatSwitchList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --SearchValue abc \
    --Status 0 \
    --VpcId abc \
    --NatId abc \
    --NatInsId abc \
    --Area abc
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "Data": [
            {
                "Id": 1,
                "SubnetId": "abc",
                "SubnetName": "abc",
                "SubnetCidr": "abc",
                "RouteId": "abc",
                "RouteName": "abc",
                "CvmNum": 1,
                "VpcId": "abc",
                "VpcName": "abc",
                "Enable": 1,
                "Status": 1,
                "NatId": "abc",
                "NatName": "abc",
                "NatInsId": "abc",
                "NatInsName": "abc",
                "Region": "abc",
                "Abnormal": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

