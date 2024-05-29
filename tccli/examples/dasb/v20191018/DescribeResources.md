**Example 1: 查询资源信息**

查询用户购买的资源信息，包括资源ID，授权点数，vpc，过期时间等。

Input: 

```
tccli dasb DescribeResources --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "rid-test",
        "ResourceSet": [
            {
                "RenewFlag": 1,
                "Zone": "ap-guangzhou-6",
                "SubnetName": "subnet-test",
                "Nodes": 1,
                "Status": 1,
                "VpcId": "vpc-test",
                "SubProductCode": "sp_cds_dasb_bh_saas",
                "ResourceId": "bh-saas-test",
                "PackageBandwidth": 1,
                "VpcName": "vpc-test",
                "ApCode": "ap-guangzhou",
                "SubnetId": "subnet-test",
                "ResourceName": "T-Sec-堡垒机（SaaS型）/专业版",
                "Expired": true,
                "Deployed": true,
                "ProductCode": "p_cds_dasb",
                "PublicIpSet": [
                    "1.1.1.1"
                ],
                "ModuleSet": [
                    "DB"
                ],
                "ExtendPoints": 1,
                "UsedNodes": 1,
                "PrivateIpSet": [
                    "1.1.1.1"
                ],
                "Pid": 1,
                "VpcCidrBlock": "192.168.0.0/16",
                "PackageNode": 1,
                "ExpireTime": "2020-09-22T00:00:00+00:00",
                "SvArgs": "sv_cds_dasb_saas_free_2node",
                "CidrBlock": "192.168.11.0/24",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "LogDeliveryArgs": ""
            }
        ]
    }
}
```

