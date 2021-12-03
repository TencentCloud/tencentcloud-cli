**Example 1: 驾驶证信息查询示例代码（姓名和身份证号一致）**



Input: 

```
tccli ocr DriverLicenseQuery --cli-unfold-argument  \
    --Name 张三 \
    --IdcardNo 4xxxxxxxxxxxxxxxx8
```

Output: 
```
{
    "Response": {
        "StartDate": "[2017-04-10 2017-06-20)",
        "EndDate": "[2018-04-10 2018-06-20)",
        "FirstIssueDate": "[2015-04-10 2015-06-20)",
        "AllowDriveCar": "C1",
        "DriveCardStatus": "正常",
        "Score": "",
        "RespCode": "0",
        "RespDesc": "姓名和身份证号一致",
        "RequestId": "2e410b72-e6e1-48dc-a955-3a5bb0ff3cee"
    }
}
```

**Example 2: 驾驶证信息查询示例代码（查询错误）**



Input: 

```
tccli ocr DriverLicenseQuery --cli-unfold-argument  \
    --Name 张三 \
    --IdcardNo 4xxxxxxxxxxxxxxxx7
```

Output: 
```
{
    "Response": {
        "StartDate": "",
        "EndDate": "",
        "FirstIssueDate": "",
        "AllowDriveCar": "",
        "DriveCardStatus": "",
        "Score": "",
        "RespCode": "-1",
        "RespDesc": "姓名和身份证号不一致",
        "RequestId": "fdfdadcb9-4924-bc27-7e57fafffD"
    }
}
```

