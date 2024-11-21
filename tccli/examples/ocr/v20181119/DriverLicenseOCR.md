**Example 1: 驾驶证正面识别示例    [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=DriverLicenseOCR)**

驾驶证识别

Input: 

```
tccli ocr DriverLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/vehicle/DriverLicenseOCR/DriverLicenseOCR1.jpg \
    --CardSide FRONT
```

Output: 
```
{
    "Response": {
        "Address": "广东省深圳市南山区腾讯大厦",
        "ArchivesCode": "",
        "CardCode": "440305198305101408",
        "Class": "C2",
        "CumulativeScore": "",
        "DateOfBirth": "1983-05-10",
        "DateOfFirstIssue": "2005-05-01",
        "EndDate": "2025-10-01",
        "IssuingAuthority": "上海市公安局交通警察总队",
        "Name": "刘洋",
        "Nationality": "中国",
        "RecognizeWarnCode": [],
        "RecognizeWarnMsg": [],
        "Record": "",
        "RequestId": "9b0d1ee9-8fdb-4194-be58-212bee88a7fd",
        "Sex": "女",
        "StartDate": "2015-10-01",
        "CurrentTime": "",
        "GenerateTime": "",
        "State": "",
        "BackPageName": "",
        "BackPageCardCode": "",
        "DriverLicenseType": ""
    }
}
```

**Example 2: 驾驶证正面告警识别示例   [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=DriverLicenseOCR)**

驾驶证识别

Input: 

```
tccli ocr DriverLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/vehicle/DriverLicenseOCR/DriverLicenseOCR2.jpg \
    --CardSide FRONT
```

Output: 
```
{
    "Response": {
        "Address": "上海市徐汇区田林路397号腾云大厦6F",
        "ArchivesCode": "",
        "CardCode": "440524198701010014",
        "Class": "C1",
        "CumulativeScore": "",
        "DateOfBirth": "1987-01-01",
        "DateOfFirstIssue": "2011-10-01",
        "EndDate": "2017-10-01",
        "IssuingAuthority": "上海市公安局交通警察总队",
        "Name": "李明",
        "Nationality": "中国",
        "RecognizeWarnCode": [
            -9102
        ],
        "RecognizeWarnMsg": [
            "WARN_DRIVER_LICENSE_COPY_CARD"
        ],
        "Record": "",
        "RequestId": "c5ceedaa-cb6f-4210-af49-0a5dee461259",
        "Sex": "男",
        "StartDate": "2011-10-01",
        "CurrentTime": "",
        "GenerateTime": "",
        "State": "",
        "BackPageName": "",
        "BackPageCardCode": "",
        "DriverLicenseType": ""
    }
}
```

**Example 3: 驾驶证反面识别示例    [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=DriverLicenseOCR)**

驾驶证反面

Input: 

```
tccli ocr DriverLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/vehicle/DriverLicenseOCR/DriverLicenseOCR2.jpg \
    --CardSide BACK
```

Output: 
```
{
    "Response": {
        "Address": "",
        "ArchivesCode": "130123421234",
        "CardCode": "130721234511112345",
        "Class": "",
        "CumulativeScore": "",
        "DateOfBirth": "",
        "DateOfFirstIssue": "",
        "EndDate": "",
        "IssuingAuthority": "",
        "Name": "李明",
        "Nationality": "",
        "RecognizeWarnCode": [],
        "RecognizeWarnMsg": [],
        "Record": "",
        "RequestId": "03023a0a-cf96-4baa-8cd8-34ba9d32f3db",
        "Sex": "",
        "StartDate": "",
        "CurrentTime": "",
        "GenerateTime": "",
        "State": "",
        "BackPageName": "",
        "BackPageCardCode": "",
        "DriverLicenseType": ""
    }
}
```

