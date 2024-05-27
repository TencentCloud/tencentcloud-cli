**Example 1: 营业执照识别示例代码**

营业执照识别示例

Input: 

```
tccli ocr BizLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Address": "深圳市南山区高新区高新南一路飞亚达大厦",
        "Angle": 0,
        "Business": "计算机软、硬件的设计、技术开发、销售(不含专营、专控、专卖商品及限制项目):数据库及计算机网络服务;国内商业、物资供销业(不含专营、专控、专卖商品)",
        "Capital": "人民币柒仟亿",
        "ComposingForm": "",
        "IsDuplication": 1,
        "Name": "深圳市腾讯计算机系统有限公司",
        "NationalEmblem": true,
        "Period": "1998年11月至长期",
        "Person": "艾米",
        "QRCode": true,
        "RecognizeWarnCode": [],
        "RecognizeWarnMsg": [],
        "RegNum": "110000012345678",
        "RegistrationAuthority": "广东省工商行政管理局",
        "RegistrationDate": "1998年11月11日",
        "RequestId": "42dbace2-9f13-4a58-ad35-aea95f0e02d7",
        "Seal": true,
        "SerialNumber": "",
        "SetDate": "1998年11月",
        "Title": "营业执照",
        "Type": "有限责任公司"
    }
}
```

