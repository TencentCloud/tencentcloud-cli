**Example 1: 查询示例**



Input: 

```
tccli waf DescribeOpUserSignatureRule --cli-unfold-argument  \
    --Domain www.test.com \
    --OpAppId 1 \
    --OpLanguage en \
    --Offset 1 \
    --Limit 20 \
    --Order asc \
    --By signature_id \
    --Filters.0.Name MainClassID \
    --Filters.0.Values 010000000 \
    --Filters.0.ExactMatch False
```

Output: 
```
{
    "Response": {
        "RequestId": "be065d7f-66f1-486d-8bd5-f203f2f303cb",
        "Total": 8,
        "Rules": [
            {
                "ID": "010000002",
                "Description": "test desc",
                "Status": 0,
                "MainClassID": "010000000",
                "MainClassName": "Cross Site Scripting",
                "SubClassID": "000000000",
                "SubClassName": "",
                "CveID": "",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ModifyTime": "2021-11-22T16:16:52+08:00",
                "Reason": 0
            },
            {
                "ID": "050000022",
                "Description": "test desc",
                "Status": 1,
                "MainClassID": "050000000",
                "MainClassName": "Cross Site Scripting",
                "SubClassID": "050030000",
                "SubClassName": "data",
                "CveID": "",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ModifyTime": "2021-11-22T16:16:52+08:00",
                "Reason": 0
            }
        ]
    }
}
```

