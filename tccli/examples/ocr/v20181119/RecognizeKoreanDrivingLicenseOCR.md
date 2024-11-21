**Example 1: 韩国驾驶证识别**

韩国驾驶证识别

Input: 

```
tccli ocr RecognizeKoreanDrivingLicenseOCR --cli-unfold-argument  \
    --ReturnHeadImage false \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg
```

Output: 
```
{
    "Response": {
        "Address": "주 소 전북 전주 덕진 반월 763-1 -籍 전주월드컵경기장28",
        "AptitudeTesDate": "28/02/2020~27/08/2020",
        "Birthday": "13/07/1987",
        "DateOfIssue": "28/02/2011",
        "ID": "7043EX",
        "LicenseNumber": "전북 11-006760-90",
        "Name": "HUANG BOWEN",
        "Number": "870713-5260590",
        "Photo": "",
        "RequestId": "4fd48a46-b911-4725-a0c4-f4be81866e12",
        "Sex": "未知",
        "Type": "2종보동"
    }
}
```

