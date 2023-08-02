**Example 1: 查询客户端的跨vpc子网访问能力**

查询客户端的跨vpc子网访问能力

Input: 

```
tccli goosefs QueryCrossVpcSubnetSupportForClientNode --cli-unfold-argument  \
    --FileSystemId x-c60-a1b2c3d4
```

Output: 
```
{
    "Response": {
        "RequestId": "b3caa32f-5e39-4360-91e4-5724369b78a6",
        "SubnetInfoCollection": [
            {
                "VpcId": "vpc-a1b2c3d4",
                "SubnetId": "subnet-a1b2c3d4"
            },
            {
                "VpcId": "vpc-h1g1d1f1",
                "SubnetId": "subnet-h1g1d1f1"
            },
            {
                "VpcId": "vpc-m1n1o1p1",
                "SubnetId": "subnet-m1n1o1p1"
            }
        ]
    }
}
```

