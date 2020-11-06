**Example 1: 获取顾客详情列表接口-成功**



Input: 

```
tccli youmall DescribePersonInfo --cli-unfold-argument  \
    --CompanyId TestCompany \
    --ShopId 1 \
    --StartPersonId 0 \
    --Offset 0 \
    --Limit 100 \
    --PersonType 1 \
    --PictureExpires 600
```

Output: 
```
{
    "Response": {
        "CompanyId": "TestCompany",
        "TotalCount": 2,
        "PersonInfoSet": [
            {
                "Age": 20,
                "Gender": 0,
                "PersonId": 1,
                "PersonType": 1,
                "PersonSubType": 1,
                "PersonPictureUrl": "xxxx"
            },
            {
                "Age": 20,
                "Gender": 0,
                "PersonId": 2,
                "PersonType": 1,
                "PersonSubType": 1,
                "PersonPictureUrl": "xxxx"
            }
        ],
        "RequestId": "6ec80684-0879-405e-8932-72e7c0c48ef8",
        "ShopId": "1"
    }
}
```

**Example 2: 获取顾客详情列表接口-失败**



Input: 

```
tccli youmall DescribePersonInfo --cli-unfold-argument  \
    --CompanyId TestCompany \
    --ShopId 1 \
    --StartPersonId 0 \
    --Offset 0 \
    --Limit 100 \
    --PersonType 1 \
    --PictureExpires 600
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "Parameter ShopId is missing"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

