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
        "RegNum": "110000012345678",
        "Person": "艾米",
        "Capital": "人民币600000万元整",
        "Name": "深圳市腾讯计算机系统有限公司",
        "Address": "深圳市南山区高新区高新南一路飞亚达大厦",
        "Period": "1998年11月至长期",
        "Business": "计算机软、硬件的设计、技术开发、销售(不含专营、专控、专卖商品及限制项目);数据库及计算机网络服务;国内商业、物资供销业(不含专营、专控、专卖商品)",
        "Type": "有限责任公司",
        "ComposingForm": "",
        "SetDate": "1998年11月",
        "Angle": 33.33,
        "IsDuplication": 1,
        "RegistrationDate": "1998年11月11日",
        "RecognizeWarnCode": [
            -9102
        ],
        "RecognizeWarnMsg": [
            "WARN_COPY_CARD"
        ],
        "RequestId": "c3025c22-e159-44fe-9850-91f30b2e2593"
    }
}
```

