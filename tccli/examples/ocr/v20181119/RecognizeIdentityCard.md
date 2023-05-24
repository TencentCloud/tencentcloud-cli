**Example 1: 身份证识别（人像面）示例代码   [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=IDCardOCR)**

身份证识别（人像面）示例代码

Input: 

```
tccli ocr RecognizeIdentityCard --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
    --CardSide FRONT
```

Output: 
```
{
    "Response": {
        "Name": "李明",
        "Sex": "男",
        "Nation": "汉",
        "Birth": "1987/1/1",
        "Address": "北京市石景山区高新技术园腾讯大楼",
        "IdNum": "440524198701010014",
        "Authority": "",
        "ValidDate": "",
        "AdvancedInfo": "{}",
        "RequestId": "ab2c132e-9e1c-43d3-b0ef-9b4d80f00330"
    }
}
```

