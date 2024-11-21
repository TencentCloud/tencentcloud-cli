**Example 1: PassportOCR调用**

PassportOCR调用   [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=PassportOCR)

Input: 

```
tccli ocr PassportOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/PassportOCR/PassportOCR1.jpg \
    --Type CN
```

Output: 
```
{
    "Response": {
        "BirthDate": "19920922",
        "BirthPlace": "SHANGHAI",
        "CodeCrc": "G123456785CHN9209220M200819219203100<<<<<<60",
        "CodeSet": "POCHNZHANG<<SAN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<",
        "Country": "CHN",
        "ExpiryDate": "20200819",
        "FamilyName": "ZHANG",
        "FirstName": "SAN",
        "IssueDate": "20100820",
        "IssuePlace": "SHANGHAI",
        "Name": "张三",
        "Nationality": "CHN",
        "PassportNo": "G12345678",
        "PortraitImageInfo": {
            "ImageCoordinates": {
                "X": 0,
                "Y": 0,
                "Width": 0,
                "Height": 0
            },
            "PortraitImage": ""
        },
        "RequestId": "c34624ee-d868-41c3-adc4-0ca09c68c9de",
        "Sex": "M",
        "Signature": ""
    }
}
```

