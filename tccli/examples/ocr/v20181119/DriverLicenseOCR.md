**Example 1: 驾驶证识别示例代码1    [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=DriverLicenseOCR)**

驾驶证识别

Input: 

```
tccli ocr DriverLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
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
        "BackPageCardCode": ""
    }
}
```

**Example 2: 驾驶证识别示例代码2    [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=DriverLicenseOCR)**

驾驶证识别

Input: 

```
tccli ocr DriverLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
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
        "BackPageCardCode": ""
    }
}
```

**Example 3: 驾驶证识别示例代码3    [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=DriverLicenseOCR)**

驾驶证反面

Input: 

```
tccli ocr DriverLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
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
        "BackPageCardCode": ""
    }
}
```

**Example 4: 驾驶证识别示例代码4    [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=DriverLicenseOCR)**

电子驾驶证识别

Input: 

```
tccli ocr DriverLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Address": "",
        "ArchivesCode": "321123405123",
        "CardCode": "321281298512340017",
        "Class": "C1",
        "CumulativeScore": "1分",
        "DateOfBirth": "1995-11-22",
        "DateOfFirstIssue": "2012-02-19",
        "EndDate": "2030-07-19",
        "IssuingAuthority": "",
        "Name": "冯妙",
        "Nationality": "中国",
        "RecognizeWarnCode": [],
        "RecognizeWarnMsg": [],
        "Record": "",
        "RequestId": "4b67dd01-c0ba-43c0-b899-e1088fa314fe",
        "Sex": "女",
        "StartDate": "2020-01-20",
        "CurrentTime": "",
        "GenerateTime": "",
        "State": "未处理",
        "BackPageName": "",
        "BackPageCardCode": ""
    }
}
```

