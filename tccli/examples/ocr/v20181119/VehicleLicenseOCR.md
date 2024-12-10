**Example 1: 行驶证主页正面识别示例**

行驶证主页正面识别示例

Input: 

```
tccli ocr VehicleLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/vehicle/VehicleLicenseOCR/VehicleLicenseOCR2.jpg \
    --CardSide FRONT
```

Output: 
```
{
    "Response": {
        "FrontInfo": {
            "PlateNo": "沪AA1234",
            "VehicleType": "小型轿车",
            "Owner": "李明",
            "Address": "上海市徐汇区田林路397号腾云大厦6F",
            "UseCharacter": "非营运",
            "Model": "别克牌SGM7151LAAA",
            "Vin": "ABCDEFGH123456789",
            "EngineNo": "8B54321",
            "RegisterDate": "2011-10-10",
            "IssueDate": "",
            "Seal": "上海市公安局交通警察总队"
        },
        "BackInfo": null,
        "RecognizeWarnCode": [
            -9102
        ],
        "RecognizeWarnMsg": [
            "WARN_DRIVER_LICENSE_COPY_CARD"
        ],
        "RequestId": "820916b4-b391-40a8-9203-7ae87e3f1954"
    }
}
```

**Example 2: 行驶证副页正面识别示例**

行驶证副页正面识别示例

Input: 

```
tccli ocr VehicleLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/vehicle/VehicleLicenseBackOCR/VehicleLicenseBackOCR1.jpg \
    --CardSide BACK
```

Output: 
```
{
    "Response": {
        "FrontInfo": null,
        "BackInfo": {
            "PlateNo": "粤B2177C",
            "FuelType": "汽油",
            "FileNo": "440681681182",
            "AllowNum": "5人",
            "TotalMass": "2085kg",
            "CurbWeight": "1610kg",
            "LoadQuality": "--",
            "ExternalSize": "4667×1839×1694mm",
            "TotalQuasiMass": "--",
            "Marks": "",
            "Record": "检验有效期至2019年11月粤E(01)汽油",
            "SubPageCode": "4460040587965"
        },
        "RecognizeWarnCode": [
            -9102
        ],
        "RecognizeWarnMsg": [
            "WARN_DRIVER_LICENSE_COPY_CARD"
        ],
        "RequestId": "e2ebfaa0-19d3-4d2b-9ed8-7c7c21eb2b74"
    }
}
```

