**Example 1: 获取用户VSM列表**



Input: 

```
tccli cloudhsm DescribeVsms --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --SearchWord xxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "7787c490-8c73-48af-bb5a-5d85cc7d4f35",
        "TotalCount": 1,
        "VsmList": [
            {
                "AlarmStatus": 0,
                "CreateUin": "2942368751",
                "ExpireTime": 1738234083,
                "Expired": false,
                "Manufacturer": "TASS",
                "Model": "SJJ1528",
                "RegionId": 1,
                "RegionName": "广州",
                "RemainSeconds": 29123420,
                "RenewFlag": 2,
                "ResourceId": "hsm-aj8fp8a0",
                "ResourceName": "default-hsmName",
                "SgList": [
                    {
                        "CreateTime": "2023-06-05 10:59:39",
                        "SgId": "sg-f51mj0kl",
                        "SgName": "casb-proxy-2023060510592885829",
                        "SgRemark": "自定义"
                    }
                ],
                "Status": 1,
                "SubnetId": "subnet-1xaztwla",
                "SubnetName": "Default-Subnet3",
                "Tags": [
                    {
                        "TagKey": "运营部门",
                        "TagValue": "测试"
                    }
                ],
                "Vip": "172.16.16.89",
                "VpcId": "vpc-7vv1q6x9",
                "VpcName": "Default-VPC",
                "VsmType": 17,
                "ZoneId": 100003,
                "ZoneName": "广州三区"
            }
        ]
    }
}
```

