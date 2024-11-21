**Example 1: HmtResidentPermitOCR调用**



Input: 

```
tccli ocr HmtResidentPermitOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/HmtResidentPermitOCR/HmtResidentPermitOCR2.png \
    --CardSide FRONT
```

Output: 
```
{
    "Response": {
        "Address": "合肥市高新区望江西路800号腾讯优图D7栋6号",
        "Authority": "",
        "Birth": "1985/2/1",
        "CardType": 0,
        "IdCardNo": "820000198502010022",
        "Name": "蓝图图",
        "PassNo": "",
        "PortraitImageInfo": {
            "ImageCoordinates": {
                "X": 0,
                "Y": 0,
                "Width": 0,
                "Height": 0
            },
            "PortraitImage": ""
        },
        "RequestId": "4685e626-f6ea-4ad8-a099-13933ea4bca9",
        "Sex": "女",
        "ValidDate": "",
        "VisaNum": "0"
    }
}
```

