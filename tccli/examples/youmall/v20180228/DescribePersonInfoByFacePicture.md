**Example 1: 根据人脸图片获取顾客身份信息**



Input: 

```
tccli youmall DescribePersonInfoByFacePicture --cli-unfold-argument  \
    --CompanyId testCompany1 \
    --ShopId 1 \
    --Picture 8ADQW312887XV878
```

Output: 
```
{
    "Response": {
        "RequestId": "6ec80684-0879-405e-8932-72e7c0c48ef8",
        "CompanyId": "testCompany1",
        "ShopId": 10086,
        "PersonId": 1,
        "PictureUrl": "http://xxx.jpg",
        "PersonType": 0,
        "FirstVisitTime": "2018-11-22 11:22:33",
        "VisitTimes": 5
    }
}
```

