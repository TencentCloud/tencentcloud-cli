**Example 1: 临时身份证告警调用示例**

临时身份证告警调用示例 [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=IDCardOCR)

Input: 

```
tccli ocr IDCardOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/IDCardOCR/IDCardOCR1.jpg \
    --Config {"TempIdWarn":true} \
    --CardSide FRONT
```

Output: 
```
{
    "Response": {
        "Address": "广东省深圳市南山区腾讯大厦",
        "AdvancedInfo": "{\"WarnInfos\":[]}",
        "Authority": "",
        "Birth": "1995/5/13",
        "IdNum": "440305199505132561",
        "Name": "刘洋",
        "Nation": "汉",
        "ReflectDetailInfos": [],
        "RequestId": "c762a670-c622-408a-865a-da27a9ffa53b",
        "Sex": "女",
        "ValidDate": ""
    }
}
```

**Example 2: 身份证照片裁剪和人像照片裁剪调用示例**

身份证照片裁剪和人像照片裁剪调用示例 [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=IDCardOCR)

Input: 

```
tccli ocr IDCardOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/IDCardOCR/IDCardOCR1.jpg \
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
        "AdvancedInfo": "{\"IdCard\":\"/9j/4AAQSkZJRg.....s97n//2Q==\",\"Portrait\":\"/9j/4AAQSkZJRg.....s97n//2Q==\"}",
        "RequestId": "97c323da-5fd3-4fe6-b0b3-1cf10b04422c"
    }
}
```

**Example 3: 身份证识别（人像面）调用示例**

身份证识别（人像面）调用示例 [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=IDCardOCR)

Input: 

```
tccli ocr IDCardOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/IDCardOCR/IDCardOCR1.jpg \
    --CardSide FRONT
```

Output: 
```
{
    "Response": {
        "Address": "广东省深圳市南山区腾讯大厦",
        "AdvancedInfo": "{\"WarnInfos\":[]}",
        "Authority": "",
        "Birth": "1995/5/13",
        "IdNum": "440305199505132561",
        "Name": "刘洋",
        "Nation": "汉",
        "ReflectDetailInfos": [],
        "RequestId": "c762a670-c622-408a-865a-da27a9ffa53b",
        "Sex": "女",
        "ValidDate": ""
    }
}
```

**Example 4: 身份证识别（国徽面）调用示例**

身份证识别（国徽面）调用示例 [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=IDCardOCR)

Input: 

```
tccli ocr IDCardOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/IDCardBackOCR/IDCardBackOCR2.jpg \
    --CardSide BACK
```

Output: 
```
{
    "Response": {
        "Address": "",
        "AdvancedInfo": "{\"WarnInfos\":[]}",
        "Authority": "上海市公安局南山分局",
        "Birth": "",
        "IdNum": "",
        "Name": "",
        "Nation": "",
        "ReflectDetailInfos": [],
        "RequestId": "c058efd9-a469-4256-a18d-bf539fd2231b",
        "Sex": "",
        "ValidDate": "2018.08.12-2038.08.12"
    }
}
```

