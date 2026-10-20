**Example 1: 查询资源信息**



Input: 

```
tccli bh DescribeResources --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ResourceSet": [
            {
                "ApCode": "ap-g****zhou",
                "BillingRegion": "ap-***ers",
                "BillingZone": "ap-o****s-4",
                "CdcClusterId": "",
                "CidrBlock": "192.1*****.0/24",
                "ClbSet": [
                    {
                        "ClbIp": "114.1*****.171"
                    }
                ],
                "ClientAccess": 1,
                "CreateTime": "2023-09-07T11:13:47+08:00",
                "DeployCvmCount": 2,
                "DeployModel": 0,
                "Deployed": true,
                "DomainCount": 0,
                "DomainName": "",
                "EnabledDomainCount": 0,
                "ExpireTime": "2027-04-28T16:44:13+08:00",
                "Expired": false,
                "ExtendPoints": 0,
                "ExternalAccess": 1,
                "IOAResource": 1,
                "IOAResourceId": "ioa-bh-0-36***********8e27f4274a",
                "IntranetAccess": 0,
                "IntranetPrivateIpSet": [],
                "IntranetSubnetId": "",
                "IntranetSubnetIdSet": null,
                "IntranetVpcCidr": "",
                "IntranetVpcId": "",
                "LbVipIsp": "",
                "LogDelivery": "",
                "LogDeliveryArgs": "",
                "ModuleSet": [],
                "Nodes": 50,
                "OpenClbId": "",
                "OrgAccountQuota": 0,
                "PackageBandwidth": 0,
                "PackageIOABandwidth": 1,
                "PackageIOAUserCount": 1,
                "PackageNode": 0,
                "PayMode": 1,
                "Pid": 1010053,
                "PrivateIpSet": [
                    "192.1*****.107"
                ],
                "ProductCode": "p_cds_dasb",
                "PublicIpSet": [
                    "114.1*****.171"
                ],
                "RenewFlag": 0,
                "ResourceEdition": "pro",
                "ResourceId": "bh-saa*****wc5mj",
                "ResourceName": "T-Sec-堡垒机（SaaS型）/专业版",
                "ResourceZoneSet": [
                    {
                        "Region": "ap-g****zhou",
                        "SubnetCidrBlock": "192.1*****.0/24",
                        "SubnetId": "subne*****vnywk",
                        "SubnetName": "subnet6",
                        "SubnetUsageType": "DEPLOY",
                        "VpcCidrBlock": "192.1*****0/16",
                        "VpcId": "vpc-****50wz",
                        "VpcName": "gord****est1",
                        "Zone": "ap-gu*****ou-6"
                    }
                ],
                "ShareClb": false,
                "Status": 1,
                "SubProductCode": "sp_cds_d********aas_pro",
                "SubnetId": "subne*****vnywk",
                "SubnetName": "sub**t6",
                "SvArgs": "sv_cds_da*********ro_50node",
                "TUICmdPort": 8300,
                "TUIDirectPort": 8300,
                "TimeSpan": 1,
                "TimeUnit": "m",
                "Trial": 0,
                "UsedDomainCount": 0,
                "UsedNodes": 1,
                "VpcCidrBlock": "192.1*****0/16",
                "VpcId": "vpc-****50wz",
                "VpcName": "gord****est1",
                "WebAccess": 1,
                "Zone": "ap-gu*****ou-6"
            }
        ],
        "TotalCount": 18,
        "RequestId": "7e4c4add-b3b2-4db0-8794-0953a4c3d9a9"
    }
}
```

