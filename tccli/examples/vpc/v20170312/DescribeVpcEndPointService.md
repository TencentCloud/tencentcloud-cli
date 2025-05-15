**Example 1: 查询终端节点服务列表**

查询终端节点服务列表

Input: 

```
tccli vpc DescribeVpcEndPointService --cli-unfold-argument  \
    --EndPointServiceIds vpcsvc-kngiybxl \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "EndPointServiceSet": [
            {
                "EndPointServiceId": "vpcsvc-kngiybxl",
                "VpcId": "vpc-cc59iepy",
                "ServiceOwner": "1308945662",
                "ServiceName": "ServiceName1",
                "ServiceVip": "9.254.118.7",
                "ServiceInstanceId": "lb-81v1v5ah",
                "AutoAcceptFlag": true,
                "EndPointCount": 1,
                "CreateTime": "2025-02-24 16:08:00",
                "ServiceType": "CLB",
                "CdcId": "",
                "TagSet": [],
                "ServiceUin": "100023008439",
                "BusinessIpType": 1,
                "EndPointSet": [
                    {
                        "ServiceName": "ServiceName1",
                        "GroupSet": [
                            "sg-6mqq4vm7"
                        ],
                        "EndPointId": "vpce-mpflh8wj",
                        "VpcId": "vpc-12fpjaso",
                        "SubnetId": "subnet-hlpwg8yh",
                        "EndPointOwner": "1308945662",
                        "EndPointName": "webhook-to-cls-fkwqdgqh-apiserver",
                        "ServiceVpcId": "vpc-cc59iepy",
                        "ServiceVip": "9.254.118.7",
                        "EndPointVip": "9.0.255.131",
                        "State": "ACTIVE",
                        "CreateTime": "2025-02-24 17:32:43",
                        "EndPointServiceId": "vpcsvc-fowynafi",
                        "CdcId": "cluster-d8htgb6k"
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "0ef824ac-e70d-4886-a777-f2ec9e184ce9"
    }
}
```

