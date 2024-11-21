**Example 1: 营业执照识别示例代码**

营业执照识别示例

Input: 

```
tccli ocr BizLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/BizLicenseOCR/BizLicenseOCR1.jpg
```

Output: 
```
{
    "Response": {
        "Address": "深圳市南山区高新区高新南一路飞亚达大厦",
        "Angle": 0.09112373739480972,
        "Business": "计算机软、硬件的设计、技术开发、销售(不含专营、专控、专卖商品及限制项目);数据库及计算机网络服务;国内商业、物资供销业(不含专营、专控、专卖商品)",
        "Capital": "人民币柒仟万",
        "ComposingForm": "",
        "Electronic": false,
        "IsDuplication": 1,
        "Name": "杭州市魔乐计算机有限公司",
        "NationalEmblem": true,
        "Period": "1998年11月至长期",
        "Person": "毛华",
        "QRCode": true,
        "RecognizeWarnCode": [],
        "RecognizeWarnMsg": [],
        "RegNum": "110000012345678",
        "RegistrationAuthority": "广东省工商行政管理局",
        "RegistrationDate": "1998年11月13日",
        "RequestId": "86356cbe-afd6-4b26-b916-7fdb1fd3a9a7",
        "Seal": true,
        "SerialNumber": "",
        "SetDate": "1998年11月",
        "Title": "营业执照",
        "Type": "有限责任公司"
    }
}
```

