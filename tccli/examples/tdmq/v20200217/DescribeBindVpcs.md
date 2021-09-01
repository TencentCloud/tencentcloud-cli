**Example 1: 获取租户VPC绑定关系**



Input: 

```
tccli tdmq DescribeBindVpcs --cli-unfold-argument  \
    --ClusterId pulsar-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "VpcSets": [
            {
                "UniqueVpcId": "vpc-c96rbu5r",
                "UniqueSubnetId": "subnet-hiqrqjp6",
                "RouterId": "pulsar-xxxxxxxx/vpc-c96rbu5r/subnet-hiqrqjp6",
                "Ip": "192.168.0.1",
                "Port": 6000,
                "Remark": ""
            }
        ],
        "TotalCount": 1,
        "RequestId": "b9765efb-62dd-4946-b2bd-61e958c0f7a7"
    }
}
```

