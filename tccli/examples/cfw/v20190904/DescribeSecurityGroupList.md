**Example 1: 查询安全组规则列表**



Input: 

```
tccli cfw DescribeSecurityGroupList --cli-unfold-argument  \
    --SearchValue {"common":"模糊检索"} \
    --Direction 1 \
    --Limit 20 \
    --Offset 0 \
    --Filter 0 \
    --Status 0 \
    --Area ap-guangzhou
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "AllTotal": 0,
        "Enable": 1,
        "Data": [
            {
                "OrderIndex": 1,
                "SourceId": "ipm-dyodhpby",
                "SourceType": 7,
                "TargetId": "subnet-fmo10koi",
                "TargetType": 2,
                "Protocol": "ANY",
                "Port": "-1/-1",
                "Strategy": 2,
                "Detail": "andy的规则",
                "BothWay": 0,
                "Id": 1,
                "Status": 1,
                "IsNew": 1,
                "VpcId": "vpc-8xuf8kf5",
                "SubnetId": "subnet-fmo10koi",
                "InstanceName": "InstanceName",
                "PublicIp": "1.1.1.1",
                "PrivateIp": "9.0.0.1",
                "Cidr": "9.0.0.1/32",
                "ServiceTemplateId": "ppmg-jz17vpis",
                "Direction": 0,
                "ProtocolPortType": 1,
                "Uuid": "cfw_sg_appid_0.0.0.0/0_17295140975391",
                "Region": "ap-guangzhou",
                "AssetGroupNameIn": "/全部资产/",
                "AssetGroupNameOut": "/全部资产/",
                "ParameterName": "自动化勿删IP组模板",
                "ProtocolPortName": "端口协议类型参数模板名称",
                "BothWayInfo": [
                    {
                        "OrderIndex": 1,
                        "SourceId": "1.1.1.1",
                        "SourceType": 7,
                        "TargetId": "1.1.1.1",
                        "TargetType": 2,
                        "Protocol": "ANY",
                        "Port": "-1/-1",
                        "Strategy": 2,
                        "Detail": "andy的规则",
                        "Status": 1,
                        "IsNew": 1,
                        "BothWay": 0,
                        "VpcId": "vpc-iedpwx01d",
                        "SubnetId": "subnet-ed2witec",
                        "InstanceName": "andy的cvm",
                        "PublicIp": "1.1.1.1",
                        "PrivateIp": "1.1.1.1",
                        "Cidr": "10.72.1.0/24",
                        "ServiceTemplateId": "pp-peodxd0e",
                        "Direction": 1,
                        "Region": "ap-guangzhou",
                        "ProtocolPortType": 1
                    }
                ]
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

