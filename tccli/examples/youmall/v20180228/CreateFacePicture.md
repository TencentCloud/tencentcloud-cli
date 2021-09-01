**Example 1: 上传人脸图片**



Input: 

```
tccli youmall CreateFacePicture --cli-unfold-argument  \
    --CompanyId testCompany1 \
    --ShopId 1 \
    --PersonType 1 \
    --Picture 8ADQW312887XV878 \
    --PictureName test.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "6ec80684-0879-405e-8932-72e7c0c48ef8",
        "PersonId": 1,
        "Status": 0,
        "PictureUrl": ""
    }
}
```

