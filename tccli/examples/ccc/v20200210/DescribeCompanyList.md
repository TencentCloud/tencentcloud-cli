**Example 1: 查询公司资质申请列表示例**



Input: 

```
tccli ccc DescribeCompanyList --cli-unfold-argument  \
    --PageSize 12 \
    --PageNumber 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "CompanyInfo": [
            {
                "Id": 1,
                "CompanyName": "北京XXX公司",
                "CreateTime": 164434242,
                "CheckTime": 154346666,
                "CheckMsg": "通过了",
                "State": 1,
                "BusinessId": "4324234323",
                "ModifyTime": 1602321412
            }
        ],
        "RequestId": "abc"
    }
}
```

