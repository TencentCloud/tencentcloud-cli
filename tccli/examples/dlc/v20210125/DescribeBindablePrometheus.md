**Example 1: 查询可绑定 Prometheus**

查询未绑定分支示例

Input: 

```
tccli dlc DescribeBindablePrometheus --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Bound": false,
        "TotalCount": 2,
        "Instances": [
            {
                "InstanceId": "prom-aaaaaaaa",
                "InstanceName": "prom-a",
                "VpcId": "vpc-xxxxxxxx",
                "SubnetId": "subnet-xxxxxxxx",
                "InstanceStatus": 2,
                "SameVpcWithTke": true
            },
            {
                "InstanceId": "prom-bbbbbbbb",
                "InstanceName": "prom-b",
                "VpcId": "vpc-yyyyyyyy",
                "SubnetId": "subnet-yyyyyyyy",
                "InstanceStatus": 2,
                "SameVpcWithTke": false
            }
        ],
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

