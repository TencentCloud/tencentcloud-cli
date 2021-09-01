**Example 1: 获取预授权规则列表**



Input: 

```
tccli bm DescribePsaRegulations --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0 \
    --OrderField CreateTime \
    --Order 1 \
    --PsaIds bm \
    --Tags.0.TagKey 测试_1 \
    --Tags.0.TagValues 到底是范德萨
```

Output: 
```
{
    "Response": {
        "RequestId": "080d4ff5-03e5-477b-9be9-3083168c86c2",
        "TotalCount": 1,
        "PsaRegulations": [
            {
                "PsaId": "bm-preauth-lswv4dgh",
                "PsaName": "到底是",
                "TagCount": 1,
                "InstanceCount": 5,
                "RepairCount": 0,
                "RepairLimit": 5,
                "CreateTime": "2018-08-28 12:56:18",
                "PsaDescription": "",
                "TaskTypeIds": [
                    30,
                    37,
                    40,
                    41,
                    44
                ],
                "Tags": [
                    {
                        "TagKey": "测试_1",
                        "TagValues": [
                            "到底是范德萨"
                        ]
                    }
                ]
            }
        ]
    }
}
```

