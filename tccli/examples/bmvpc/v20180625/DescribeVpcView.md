**Example 1: 查询黑石VPC视图**

查询黑石VPC视图

Input: 

```
tccli bmvpc DescribeVpcView --cli-unfold-argument  \
    --VpcId vpc-ox7p0l9u
```

Output: 
```
{
    "Response": {
        "VpcView": {
            "VpcId": "vpc-ox7p0l9u",
            "VpcName": "test",
            "CidrBlock": "10.0.0.0/16",
            "Zone": "ap-guangzhoutest-blsh3-1",
            "LbNum": 0,
            "EipNum": 0,
            "NatNum": 0,
            "SubnetSet": [
                {
                    "SubnetId": "subnet-fgorv065",
                    "SubnetName": "fda",
                    "CidrBlock": "10.0.0.0/17",
                    "CpmNum": 0,
                    "LbNum": 0,
                    "Zone": "ap-guangzhoutest-blsh3-1"
                }
            ]
        },
        "RequestId": "c2e83630-6084-44ef-8478-07340d0f5170"
    }
}
```

