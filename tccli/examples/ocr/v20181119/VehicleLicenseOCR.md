**Example 1: 行驶证主页正面识别示例代码1**

行驶证主页正面识别示例代码1

Input: 

```
tccli ocr VehicleLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
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
            "Seal": "上海市公安局交通警寨总队"
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

**Example 2: 行驶证副页正面识别示例代码2**

行驶证副页正面识别示例代码2

Input: 

```
tccli ocr VehicleLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
    --CardSide BACK
```

Output: 
```
{
    "Response": {
        "FrontInfo": null,
        "BackInfo": {
            "PlateNo": "皖AC4L50",
            "FileNo": "A00-00476807",
            "AllowNum": "5人",
            "TotalMass": "1837kg",
            "CurbWeight": "1431kg",
            "LoadQuality": "--",
            "ExternalSize": "4620×1780×1498mm",
            "TotalQuasiMass": "--",
            "Marks": "",
            "Record": "检验有效期至2015年11月皖A(4S)",
            "SubPageCode": ""
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

**Example 3: 行驶证副页正面识别示例代码3**

行驶证副页正面识别示例代码3

Input: 

```
tccli ocr VehicleLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
    --CardSide BACK
```

Output: 
```
{
    "Response": {
        "FrontInfo": null,
        "BackInfo": {
            "PlateNo": "皖AC4L50",
            "FileNo": "A00-00476807",
            "AllowNum": "5人",
            "TotalMass": "1837kg",
            "CurbWeight": "1431kg",
            "LoadQuality": "--",
            "ExternalSize": "4620×1780×1498mm",
            "TotalQuasiMass": "--",
            "Marks": "",
            "Record": "检验有效期至2015年11月皖A(4S)",
            "SubPageCode": ""
        },
        "RecognizeWarnCode": [
            -9103
        ],
        "RecognizeWarnMsg": [
            "WARN_DRIVER_LICENSE_SCREENED_CARD"
        ],
        "RequestId": "e2ebfaa0-19d3-4d2b-9ed8-7c7c21eb2b74"
    }
}
```

