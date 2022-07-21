**Example 1: 用于获取弹性网卡的信息**



Input: 

```
tccli vpc DescribeEniInternal --cli-unfold-argument  \
    --Limit 100 \
    --UniqueEniId eniid \
    --VpcId 1 \
    --EniId 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 2,
        "EniSet": [
            {
                "VpcId": 78257,
                "EniId": 2660066,
                "UniqueEniId": "eni-kj7karc5",
                "UniqueVpcId": "vpc-jmaywf6r",
                "Description": "xxx",
                "Mac": "20:90:6F:BF:08:D2",
                "Business": "xxx",
                "Owner": "251198225",
                "State": 1,
                "UniqueSubnetId": "subnet-dbrazzr0",
                "ElasticNetworkCardName": "veni_vFspLEfU",
                "SubnetId": 1990867,
                "BusinessOwner": "xxx",
                "ArpLearningFlag": 1,
                "Type": 0,
                "CreateTime": "2021-07-06 09:52:34",
                "Name": "TEST"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

