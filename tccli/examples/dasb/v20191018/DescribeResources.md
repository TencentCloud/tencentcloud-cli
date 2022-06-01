**Example 1: 查询资源信息**

查询用户购买的资源信息，包括资源ID，授权点数，vpc，过期时间等。

Input: 

```
tccli dasb DescribeResources --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "ResourceSet": [
            {
                "RenewFlag": 1,
                "Zone": "xx",
                "SubnetName": "xx",
                "Nodes": 1,
                "Status": 1,
                "VpcId": "xx",
                "SubProductCode": "xx",
                "ResourceId": "xx",
                "PackageBandwidth": 1,
                "VpcName": "xx",
                "ApCode": "xx",
                "SubnetId": "xx",
                "ResourceName": "xx",
                "Expired": true,
                "Deployed": true,
                "ProductCode": "xx",
                "PublicIpSet": [
                    "xx"
                ],
                "ModuleSet": [
                    "xx"
                ],
                "ExtendPoints": 1,
                "UsedNodes": 1,
                "PrivateIpSet": [
                    "xx"
                ],
                "Pid": 1,
                "VpcCidrBlock": "xx",
                "PackageNode": 1,
                "ExpireTime": "2020-09-22T00:00:00+00:00",
                "SvArgs": "xx",
                "CidrBlock": "xx",
                "CreateTime": "2020-09-22T00:00:00+00:00"
            }
        ]
    }
}
```

