**Example 1: 查询公司列表**



Input: 

```
tccli ssl DescribeCompanies --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Companies": [
            {
                "CompanyId": 122,
                "CompanyName": "腾讯",
                "CompanyCountry": "中国",
                "CompanyProvince": "广东",
                "CompanyCity": "深圳",
                "CompanyAddress": "深南大道",
                "CompanyPhone": "2132323"
            }
        ],
        "RequestId": "5779b652-9c64-45b3-a6f4-641db7376a2e"
    }
}
```

