**Example 1: 查询终端节点列表**

查询终端节点列表

Input: 

```
tccli vpc DescribeVpcEndPoint --cli-unfold-argument  \
    --Limit 1 \
    --EndPointId vpce-h0fk8lfc \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "EndPointSet": [
            {
                "EndPointId": "vpce-h0fk8lfc",
                "VpcId": "vpc-fayu2933",
                "SubnetId": "subnet-5wwu8jak",
                "EndPointOwner": "1308945662",
                "EndPointName": "webhook-to-cls-4b4uruv7-apiserver",
                "ServiceVpcId": "vpc-iqgxgqs5",
                "ServiceVip": "9.254.45.8",
                "EndPointServiceId": "vpcsvc-53c3e41h",
                "EndPointVip": "9.4.255.99",
                "State": "ACTIVE",
                "CreateTime": "2024-12-12 15:57:24",
                "GroupSet": [
                    "sg-6mqq4vm7"
                ],
                "ServiceName": "cls-4b4uruv7-apiserver",
                "CdcId": "cluster-d8htgb6k",
                "TagSet": [
                    {
                        "Key": "Key1",
                        "Value": "Value1"
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "7cb47b93-0e04-4310-b100-80fc6c06e513"
    }
}
```

