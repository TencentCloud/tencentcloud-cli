**Example 1: 驾驶证识别示例代码1    [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=DriverLicenseOCR)**



Input: 

```
tccli ocr DriverLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg\
    --CardSide FRONT
```

Output: 
```
{
    "Response": {
        "Name": "李明",
        "Sex": "男",
        "Nationality": "中国",
        "Address": "上海市徐汇区田林路397号腾云大厦6F",
        "DateOfBirth": "1987-01-01",
        "DateOfFirstIssue": "2011-10-01",
        "Class": "C1",
        "StartDate": "2011-10-01",
        "EndDate": "2017-10-01",
        "CardCode": "440524198701010014",
        "ArchivesCode": "",
        "Record": "",
        "RecognizeWarnCode": [
            -9106
        ],
        "RecognizeWarnMsg": [
            "WARN_DRIVER_LICENSE_PS_CARD"
        ],
        "RequestId": "4ba2958b-e7cf-41c2-aafe-fdc985307f63"
    }
}
```

**Example 2: 驾驶证识别示例代码2    [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=DriverLicenseOCR)**



Input: 

```
tccli ocr DriverLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg\
    --CardSide FRONT
```

Output: 
```
{
    "Response": {
        "Name": "李四",
        "Sex": "男",
        "Nationality": "中国",
        "Address": "上海市徐汇区田林路397号腾云大厦3F",
        "DateOfBirth": "1989-01-01",
        "DateOfFirstIssue": "2012-10-01",
        "Class": "C1",
        "StartDate": "2011-10-01",
        "EndDate": "2017-10-01",
        "CardCode": "440xxxxxxxxxxx0011",
        "ArchivesCode": "",
        "Record": "",
        "RecognizeWarnCode": [
            -9106,
            -9103
        ],
        "RecognizeWarnMsg": [
            "WARN_DRIVER_LICENSE_PS_CARD",
            "WARN_DRIVER_LICENSE_SCREENED_CARD"
        ],
        "RequestId": "4ba2958b-e7cf-41c2-aafe-fdc985307f63"
    }
}
```

**Example 3: 驾驶证识别示例代码3    [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=DriverLicenseOCR)**



Input: 

```
tccli ocr DriverLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg\
    --CardSide BACK
```

Output: 
```
{
    "Response": {
        "Name": "文磊",
        "Sex": "",
        "Nationality": "",
        "Address": "",
        "DateOfBirth": "",
        "DateOfFirstIssue": "",
        "Class": "",
        "StartDate": "",
        "EndDate": "",
        "CardCode": "510106197906030018",
        "ArchivesCode": "510111425293",
        "Record": "",
        "RecognizeWarnCode": [],
        "RecognizeWarnMsg": [],
        "RequestId": "83e87a88-2382-4781-96ec-f8d620fffee8"
    }
}
```

**Example 4: 驾驶证识别示例代码4    [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=DriverLicenseOCR)**



Input: 

```
tccli ocr DriverLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg\
    --CardSide BACK
```

Output: 
```
{
    "Response": {
        "Name": "文磊",
        "Sex": "",
        "Nationality": "",
        "Address": "",
        "DateOfBirth": "",
        "DateOfFirstIssue": "",
        "Class": "",
        "StartDate": "",
        "EndDate": "",
        "CardCode": "510106197906030018",
        "ArchivesCode": "510111425293",
        "Record": "",
        "RecognizeWarnCode": [
            -9106,
            -9103
        ],
        "RecognizeWarnMsg": [
            "WARN_DRIVER_LICENSE_PS_CARD",
            "WARN_DRIVER_LICENSE_SCREENED_CARD"
        ],
        "RequestId": "83e87a88-2382-4781-96ec-f8d620fffee8"
    }
}
```

