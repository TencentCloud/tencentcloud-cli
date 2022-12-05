**Example 1: 获取CC精准防护列表**



Input: 

```
tccli antiddos DescribeCCPrecisionPlyList --cli-unfold-argument  \
    --Business bgp-multip \
    --InstanceId bgp-00000211 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "23a97c66-22d4-4522-b93b-388aac08777d",
        "Total": 1,
        "PrecisionPolicyList": [
            {
                "PolicyId": "ccPrecs-00000001",
                "InstanceId": "bgp-00000211",
                "Ip": "1.1.1.1",
                "Protocol": "http",
                "Domain": "www.test.com",
                "PolicyAction": "alg",
                "PolicyList": [
                    {
                        "FieldType": "value",
                        "FieldName": "cgi",
                        "Value": "test",
                        "ValueOperator": "include"
                    }
                ],
                "CreateTime": "2022-12-01 09:05:36",
                "ModifyTime": "2022-12-01 09:05:36"
            }
        ]
    }
}
```

