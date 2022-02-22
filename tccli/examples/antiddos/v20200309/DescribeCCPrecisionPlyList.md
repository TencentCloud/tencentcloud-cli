**Example 1: 获取CC精准防护列表**



Input: 

```
tccli antiddos DescribeCCPrecisionPlyList --cli-unfold-argument  \
    --Domain xx \
    --Protocol xx \
    --Business xx \
    --InstanceId xx \
    --Ip xx \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "PrecisionPolicyList": [
            {
                "Domain": "xx",
                "PolicyAction": "xx",
                "InstanceId": "xx",
                "Ip": "xx",
                "PolicyList": [
                    {
                        "ValueOperator": "xx",
                        "FieldName": "xx",
                        "FieldType": "xx",
                        "Value": "xx"
                    }
                ],
                "PolicyId": "xx",
                "ModifyTime": "2020-09-22 00:00:00",
                "Protocol": "xx",
                "CreateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "xx"
    }
}
```

