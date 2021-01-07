**Example 1: 查询安全组规则列表**



Input: 

```
tccli cfw DescribeSecurityGroupList --cli-unfold-argument  \
    --SearchValue  \
    --Direction 1 \
    --Limit 20 \
    --Offset 0 \
    --Filter 0 \
    --Status  \
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
                "Status": 1,
                "TargetType": 1,
                "VpcId": "vpc-khmhp1co1",
                "Protocol": "ANY",
                "SourceType": 1,
                "IsNew": 1,
                "SourceId": "ins-1kub1g5f",
                "Port": "-1/-1",
                "TargetId": "0.0.0.0/0",
                "Detail": "添加规则test",
                "PrivateIp": "172.27.0.17",
                "PublicIp": "119.27.187.24",
                "OrderIndex": 1,
                "SubnetId": "subnet-9qs6catf",
                "Cidr": "",
                "Strategy": 1,
                "InstanceName": "成都多协议-勿删（勿删勿删勿删勿删）",
                "Id": 1,
                "BothWay": 1
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

