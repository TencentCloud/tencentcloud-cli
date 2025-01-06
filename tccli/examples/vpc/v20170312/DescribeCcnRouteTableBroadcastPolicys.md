**Example 1: 查询云联网路由传播策略**

查询云联网路由传播策略

Input: 

```
tccli vpc DescribeCcnRouteTableBroadcastPolicys --cli-unfold-argument  \
    --CcnId ccn-qd6z2ld1 \
    --RouteTableId ccnrtb-1mkezrkd \
    --PolicyVersion 5
```

Output: 
```
{
    "Response": {
        "PolicySet": [
            {
                "Policys": [
                    {
                        "RouteConditions": [
                            {
                                "Name": "instance-region",
                                "Values": [
                                    "ap-beijing"
                                ],
                                "MatchPattern": 1
                            },
                            {
                                "Name": "cidr-block",
                                "Values": [
                                    "9.0.0.0/8",
                                    "10.0.0.0/8",
                                    "192.168.0.0/24"
                                ],
                                "MatchPattern": 0
                            }
                        ],
                        "BroadcastConditions": [
                            {
                                "Name": "instance-region",
                                "Values": [
                                    "ap-beijing"
                                ],
                                "MatchPattern": 1
                            },
                            {
                                "Name": "instance-type",
                                "Values": [
                                    "VPC"
                                ],
                                "MatchPattern": 1
                            },
                            {
                                "Name": "instance-id",
                                "Values": [
                                    "vpc-jdevjrup",
                                    "vpc-hb81v349"
                                ],
                                "MatchPattern": 1
                            }
                        ],
                        "Action": "accept",
                        "Description": "允许接受北京地域专线、VPC、VPN三大网段"
                    },
                    {
                        "RouteConditions": [
                            {
                                "Name": "instance-type",
                                "Values": [
                                    "VPC",
                                    "DIRECTCONNECT"
                                ],
                                "MatchPattern": 1
                            },
                            {
                                "Name": "instance-id",
                                "Values": [
                                    "dcg-8zljkrft",
                                    "vpc-jdevjrup"
                                ],
                                "MatchPattern": 1
                            }
                        ],
                        "BroadcastConditions": [
                            {
                                "Name": "instance-id",
                                "Values": [
                                    "vpc-jdevjrup",
                                    "vpc-hb81v349"
                                ],
                                "MatchPattern": 1
                            }
                        ],
                        "Action": "accept",
                        "Description": "指定vpc接受北京指定专线和vpc"
                    }
                ],
                "PolicyVersion": 5,
                "CreateTime": "2022-12-19 19:31:17"
            }
        ],
        "TotalCount": 1,
        "RequestId": "da0f5fee-14f5-4429-85b3-6650beaa6b46"
    }
}
```

