**Example 1: RideHailingTransportLicenseOCR调用**



Input: 

```
tccli ocr RideHailingTransportLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg
```

Output: 
```
{
    "Response": {
        "EndDate": "2031年05月31日",
        "OperationLicenseNumber": "川交运管许可字88888888",
        "ReleaseDate": "20年月05日28",
        "RequestId": "6d930f3a-46fd-43b2-8557-cd685cd618e2",
        "StartDate": "2024年07月23日",
        "VehicleNumber": "腾讯牌AAA8888AAAAA8",
        "VehicleOwner": "腾讯云有限公司"
    }
}
```

