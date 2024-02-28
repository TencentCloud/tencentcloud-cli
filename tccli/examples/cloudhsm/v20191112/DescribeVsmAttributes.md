**Example 1: 获取VSM属性**

获取VSM属性

Input: 

```
tccli cloudhsm DescribeVsmAttributes --cli-unfold-argument  \
    --ResourceId hsm-aj8fp8a0
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1738234083,
        "Expired": false,
        "Manufacturer": "TASS",
        "Model": "SJJ1528",
        "RegionId": 1,
        "RegionName": "广州",
        "RemainSeconds": 29124028,
        "RenewFlag": 2,
        "RequestId": "98119ebc-93c2-43c6-b0db-be2efdf93ffb",
        "ResourceId": "hsm-aj8fp8a0",
        "ResourceName": "default-hsmName",
        "SgList": [
            {
                "CreateTime": "2023-06-05 10:59:39",
                "InBound": [
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "Desc": "一键放通入站规则",
                        "Id": "",
                        "Ip": "0.0.0.0/0",
                        "Port": "20,21,22,3389,80,443",
                        "Proto": "tcp",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "Desc": "一键放通入站规则",
                        "Id": "",
                        "Ip": "0.0.0.0/0",
                        "Port": "ALL",
                        "Proto": "ALL",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "Desc": "",
                        "Id": "",
                        "Ip": "172.16.0.0/16",
                        "Port": "ALL",
                        "Proto": "ALL",
                        "ServiceModule": ""
                    }
                ],
                "OutBound": [
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "Desc": "放通所有",
                        "Id": "",
                        "Ip": "0.0.0.0/0",
                        "Port": "ALL",
                        "Proto": "ALL",
                        "ServiceModule": ""
                    }
                ],
                "SgId": "sg-f51mj0kl",
                "SgName": "casb-proxy-2023060510592885829",
                "SgRemark": "自定义",
                "Version": 0
            }
        ],
        "Status": 1,
        "SubnetCidrBlock": "172.16.16.0/20",
        "SubnetId": "subnet-1xaztwla",
        "SubnetName": "Default-Subnet3",
        "Tags": [
            {
                "TagKey": "运营部门",
                "TagValue": "测试"
            }
        ],
        "Vip": "172.16.16.89",
        "VpcCidrBlock": "172.16.0.0/16",
        "VpcId": "vpc-7vv1q6x9",
        "VpcName": "Default-VPC",
        "VsmType": 17,
        "ZoneId": 100003,
        "ZoneName": "广州三区"
    }
}
```

