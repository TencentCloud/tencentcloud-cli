**Example 1: 查询示例**

查询示例

Input: 

```
tccli waf DescribeUserSignatureRule --cli-unfold-argument  \
    --Domain qcloudwaf.com \
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
                "ID": "0100000",
                "Status": 0,
                "MainClassID": "02000000",
                "SubClassID": "03000000",
                "CveID": "cve-11111",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ModifyTime": "2020-09-22T00:00:00+00:00",
                "MainClassName": "xss",
                "SubClassName": "xss-1",
                "Description": "xss",
                "Reason": 0,
                "RiskLevel": 0
            }
        ],
        "RequestId": "xxx-iiiiii"
    }
}
```

