**Example 1: 查询示例**

查询示例

Input: 

```
tccli waf DescribeUserSignatureRule --cli-unfold-argument  \
    --Domain  \
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
        "Total": 1,
        "Rules": [
            {
                "ID": "abc",
                "Status": 0,
                "MainClassID": "abc",
                "SubClassID": "abc",
                "CveID": "abc",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ModifyTime": "2020-09-22T00:00:00+00:00",
                "MainClassName": "abc",
                "SubClassName": "abc",
                "Description": "abc",
                "Reason": 0,
                "RiskLevel": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

