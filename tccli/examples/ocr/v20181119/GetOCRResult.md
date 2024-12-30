**Example 1: 获取ocr结果**

获取ocr结果

Input: 

```
tccli ocr GetOCRResult --cli-unfold-argument  \
    --OCRToken 754119FD-511F-4EF5-ADBC-F271AE62F908
```

Output: 
```
{
    "Response": {
        "OCRResult": {
            "IDCardResult": {
                "Back": {
                    "Authority": "上海市公安局静安分局",
                    "ErrorCode": "Success",
                    "ErrorMessage": "成功",
                    "RequestId": "51b411c9-7dd9-430f-8307-9435d28748b6",
                    "ValidDate": "2008.09.08-2028.09.08",
                    "WarnCodes": [
                        -9102,
                        -9101
                    ]
                },
                "Front": {
                    "Address": "北京市海淀区知春路1号2栋3号",
                    "Birth": "1999/5/7",
                    "ErrorCode": "Success",
                    "ErrorMessage": "成功",
                    "IdNum": "110129199905070025",
                    "Name": "侯小珂",
                    "Nation": "汉",
                    "RequestId": "64248e56-e24b-424b-8c07-3672bd58d24b",
                    "Sex": "女",
                    "WarnCodes": [
                        -9102,
                        -9101,
                        -9106
                    ]
                }
            }
        },
        "RequestId": "ff4412d0-abf0-4560-8f65-cc46b190c0eb",
        "Type": "IDCardOCR"
    }
}
```

