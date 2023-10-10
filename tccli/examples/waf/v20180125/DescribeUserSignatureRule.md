**Example 1: 查询示例**



Input: 

```
tccli waf DescribeUserSignatureRule --cli-unfold-argument  \
    --Domain xx \
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
        "RequestId": "xx",
        "Total": 8,
        "Rules": [
            {
                "ID": "010000002",
                "Description": "xx",
                "Status": 0,
                "MainClassID": "010000000",
                "MainClassName": "Cross Site Scripting",
                "SubClassID": "000000000",
                "SubClassName": "",
                "CveID": "",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ModifyTime": "2021-11-22T16:16:52+08:00"
            },
            {
                "ID": "050000022",
                "Description": "xx",
                "Status": 1,
                "MainClassID": "050000000",
                "MainClassName": "Cross Site Scripting",
                "SubClassID": "050030000",
                "SubClassName": "data",
                "CveID": "",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ModifyTime": "2021-11-22T16:16:52+08:00"
            }
        ]
    }
}
```

