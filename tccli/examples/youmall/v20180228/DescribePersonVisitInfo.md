**Example 1: 获取顾客到访信息列表接口-成功**



Input: 

```
tccli youmall DescribePersonVisitInfo --cli-unfold-argument  \
    --CompanyId testCompany1 \
    --ShopId 1 \
    --StartDateTime '2016-10-10 00:00:10' \
    --EndDateTime '2017-06-01 00:00:10' \
    --Offset 100 \
    --Limit 100 \
    --PictureExpires 10
```

Output: 
```
{
    "Response": {
        "CompanyId": "testCompany1",
        "TotalCount": 2,
        "PersonVisitInfoSet": [
            {
                "CapturedPictureUrl": "xxx",
                "GlassType": 1,
                "HairType": 2,
                "InTime": 1529565964,
                "MaskType": 0,
                "PersonId": 1,
                "VisitId": 123
            },
            {
                "CapturedPictureUrl": "xxx",
                "GlassType": 1,
                "HairType": 2,
                "InTime": 1529565964,
                "MaskType": 0,
                "PersonId": 1,
                "VisitId": 123
            }
        ],
        "RequestId": "6ec80684-0879-405e-8932-72e7c0c48ef8",
        "ShopId": 1
    }
}
```

**Example 2: 获取顾客到访信息列表接口-失败**



Input: 

```
tccli youmall DescribePersonVisitInfo --cli-unfold-argument  \
    --CompanyId testCompany1 \
    --ShopId 1 \
    --StartDateTime '2016-10-10 00:00:10' \
    --EndDateTime '2017-06-01 00:00:10' \
    --Offset 100 \
    --Limit 100 \
    --PictureExpires 10
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "Parameter CompanyId is missing"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

