**Example 1: 查询许可列表**



Input: 

```
tccli tsf DescribeLicenses --cli-unfold-argument  \
    --Offset 0 \
    --Limit 50
```

Output: 
```
{
    "Response": {
        "RequestId": "6d7e580e-4b1c-49a7-8ffd-21551f865643",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "LicenseId": "tsf-jhdas5d3",
                    "Tags": [
                        {
                            "TagKey": "",
                            "TagValue": "AAA"
                        },
                        {
                            "TagKey": "",
                            "TagValue": "BBB"
                        }
                    ]
                }
            ]
        }
    }
}
```

