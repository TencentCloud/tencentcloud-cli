**Example 1: demo**



Input: 

```
tccli vpc DescribeTrunkingSubEniInternal --cli-unfold-argument  \
    --UniqueTrunkingEniId eni-0sf0voxx
```

Output: 
```
{
    "Response": {
        "Total": 4,
        "GetTrunkingSubEniResult": [
            {
                "TrunkingEniId": 5427863,
                "VpcId": 5357294,
                "EniId": 5428502,
                "UniqueEniId": "eni-dyino2a7",
                "UniqueVpcId": "vpc-a18fo1wt",
                "VlanId": 2523,
                "Owner": "251229581_skip",
                "UniqueSubnetId": "subnet-l92bfblq",
                "UniqueTrunkingEniId": "eni-0sf0voxx",
                "SubnetId": 2200050,
                "TrunkingSubEniId": 10761,
                "CreateTime": "2022-11-08 22:14:14"
            },
            {
                "TrunkingEniId": 5427863,
                "VpcId": 5357294,
                "EniId": 5437236,
                "UniqueEniId": "eni-io4xd3xj",
                "UniqueVpcId": "vpc-a18fo1wt",
                "VlanId": 2049,
                "Owner": "251229581_skip",
                "UniqueSubnetId": "subnet-rwkvb5to",
                "UniqueTrunkingEniId": "eni-0sf0voxx",
                "SubnetId": 2200053,
                "TrunkingSubEniId": 10848,
                "CreateTime": "2022-11-10 15:43:48"
            },
            {
                "TrunkingEniId": 5427863,
                "VpcId": 5352363,
                "EniId": 5427874,
                "UniqueEniId": "eni-izs2hwef",
                "UniqueVpcId": "vpc-a6vkz48b",
                "VlanId": 514,
                "Owner": "251229581_skip",
                "UniqueSubnetId": "subnet-q5opw5mk",
                "UniqueTrunkingEniId": "eni-0sf0voxx",
                "SubnetId": 2200301,
                "TrunkingSubEniId": 10732,
                "CreateTime": "2022-11-08 17:55:44"
            },
            {
                "TrunkingEniId": 5427863,
                "VpcId": 5357294,
                "EniId": 5431875,
                "UniqueEniId": "eni-k2xymg15",
                "UniqueVpcId": "vpc-a18fo1wt",
                "VlanId": 691,
                "Owner": "251229581_skip",
                "UniqueSubnetId": "subnet-dkl2tqtw",
                "UniqueTrunkingEniId": "eni-0sf0voxx",
                "SubnetId": 2200597,
                "TrunkingSubEniId": 10767,
                "CreateTime": "2022-11-09 11:12:44"
            }
        ],
        "RequestId": "6ea7593e-ea56-4ab4-a33d-327b348e764c"
    }
}
```

