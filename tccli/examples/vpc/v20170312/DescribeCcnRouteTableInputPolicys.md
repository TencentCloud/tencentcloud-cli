**Example 1: DescribeCcnRouteTableInputPolicys**

查询路由表接收策略

Input: 

```
tccli vpc DescribeCcnRouteTableInputPolicys --cli-unfold-argument  \
    --CcnId ccn-rxz9krjj \
    --RouteTableId ccnrtb-63ujxv2h \
    --PolicyVersion 1
```

Output: 
```
{
    "Response": {
        "PolicySet": [
            {
                "Policys": [],
                "PolicyVersion": 29,
                "CreateTime": "2023-05-16 16:13:39"
            },
            {
                "Policys": [
                    {
                        "RouteConditions": [
                            {
                                "Name": "instance-type",
                                "Values": [
                                    "DIRECTCONNECT",
                                    "VPNGW"
                                ],
                                "MatchPattern": 1
                            }
                        ],
                        "Action": "accept",
                        "Description": ""
                    }
                ],
                "PolicyVersion": 28,
                "CreateTime": "2023-05-16 16:13:32"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

