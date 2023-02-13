**Example 1: 查询VPC下的云主机实例列表**

查询VPC下的云主机实例列表

Input: 

```
tccli vpc DescribeVpcInstances --cli-unfold-argument  \
    --Filters.0.Name vpc-id \
    --Filters.0.Values vpc-12345678 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "VpcId": "vpc-12345678",
                "SubnetId": "subnet-12345678",
                "InstanceId": "ins-12345678",
                "InstanceName": "test",
                "InstanceState": "RUNNING",
                "InstanceType": "S2.SMALL2",
                "CPU": 1,
                "Memory": 1,
                "EniLimit": 2,
                "EniIpLimit": 2,
                "InstanceEniCount": 1,
                "CreatedTime": "2020-01-01 10:00:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

