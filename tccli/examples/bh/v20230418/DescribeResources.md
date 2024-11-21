**Example 1: 查询资源信息**

查询用户购买的资源信息，包括资源ID，授权点数，vpc，过期时间等。

Input: 

```
tccli bh DescribeResources --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082",
        "ResourceSet": [
            {
                "RenewFlag": 1,
                "Zone": "us-west-2",
                "SubnetName": "subnet-01abc23d",
                "Nodes": 3,
                "Status": 1,
                "VpcId": "vpc-0abcd12ef",
                "SubProductCode": "ec2",
                "ResourceId": "i-0abcd1234efgh5678",
                "PackageBandwidth": 100,
                "VpcName": "my-vpc",
                "ApCode": "ap-1234",
                "SubnetId": "subnet-01abc23d",
                "ResourceName": "my-resource",
                "Expired": false,
                "Deployed": true,
                "ProductCode": "aws",
                "PublicIpSet": [
                    "203.0.113.0"
                ],
                "ModuleSet": [
                    "module-1"
                ],
                "ExtendPoints": 2,
                "UsedNodes": 2,
                "PrivateIpSet": [
                    "10.0.0.1"
                ],
                "Pid": 1234,
                "VpcCidrBlock": "10.0.0.0/16",
                "PackageNode": 1,
                "ExpireTime": "2022-12-31T00:00:00+00:00",
                "SvArgs": "arg1,arg2,arg3",
                "CidrBlock": "10.0.1.0/24",
                "CreateTime": "2021-01-01T00:00:00+00:00",
                "LogDeliveryArgs": "LogDeliveryArgsTest"
            }
        ]
    }
}
```

