**Example 1: 临时身份证告警示例代码**

临时身份证告警示例代码 [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=IDCardOCR)

Input: 

```
tccli ocr IDCardOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
    --Config {"TempIdWarn":true} \
    --CardSide FRONT
```

Output: 
```
{
    "Response": {
        "Name": "",
        "Sex": "",
        "Nation": "",
        "Birth": "",
        "Address": "",
        "IdNum": "",
        "Authority": "",
        "ValidDate": "",
        "ReflectDetailInfos": [],
        "AdvancedInfo": "{\"WarnInfos\":[-9104]}",
        "RequestId": "sd33222eqd1dqq948487"
    }
}
```

**Example 2: 身份证照片裁剪和人像照片裁剪示例代码**

身份证照片裁剪和人像照片裁剪示例代码 [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=IDCardOCR)

Input: 

```
tccli ocr IDCardOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
    --Config {"CropIdCard":true,"CropPortrait":true} \
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
        "ReflectDetailInfos": [],
        "AdvancedInfo": "{\"IdCard\":\"/9j/4AAA.........\",\"Portrait\":\"/9j/4AAQSkZJRBA=...........\"}",
        "RequestId": "97c323da-5fd3-4fe6-b0b3-1cf10b04422c"
    }
}
```

**Example 3: 身份证识别（人像面）示例代码**

身份证识别（人像面）示例代码 [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=IDCardOCR)

Input: 

```
tccli ocr IDCardOCR --cli-unfold-argument  \
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
        "ReflectDetailInfos": [],
        "RequestId": "ab2c132e-9e1c-43d3-b0ef-9b4d80f00330"
    }
}
```

**Example 4: 身份证识别（国徽面）示例代码**

身份证识别（国徽面）示例代码 [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=IDCardOCR)

Input: 

```
tccli ocr IDCardOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
    --CardSide BACK
```

Output: 
```
{
    "Response": {
        "Name": "",
        "Sex": "",
        "Nation": "",
        "Birth": "",
        "Address": "",
        "IdNum": "",
        "Authority": "赵县公安局",
        "ValidDate": "2010.07.21-2020.07.21",
        "AdvancedInfo": "{}",
        "ReflectDetailInfos": [],
        "RequestId": "0d394478-6d4d-48fc-8b19-552415bf46de"
    }
}
```

