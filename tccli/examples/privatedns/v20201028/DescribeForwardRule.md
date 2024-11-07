**Example 1: 查询转发规则**



Input: 

```
tccli privatedns DescribeForwardRule --cli-unfold-argument  \
    --RuleId fid-af2f9nkug
```

Output: 
```
{
    "Response": {
        "RequestId": "5cd964e2-b5e6-8a35-9ce5a1085860c845",
        "ForwardRule": {
            "Domain": "qq.com",
            "ZoneId": "zone-s8cs72d9",
            "RuleId": "fid-fa2c8misu",
            "ForwardAddress": [
                "1.1.11.1:53"
            ],
            "RuleType": "DOWN",
            "VpcSet": [
                {
                    "Region": "ap-guangzhou",
                    "UniqVpcId": "vpc-as3bsfml"
                }
            ],
            "EndPointName": "终端节点名",
            "EndPointId": "eid-fc9iuxhg4",
            "RuleName": "转发规则名称",
            "UpdatedAt": "2022-09-09 10:45:44",
            "CreatedAt": "2022-09-09 10:45:44"
        }
    }
}
```

