**Example 1: 马来西亚身份证识别示例代码**



Input: 

```
tccli ocr MLIDCardOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Name": "KAVIN ONG KHI MN",
        "ID": "710716-08-6085",
        "Address": "NO 11 PERSIARN PERAJRIT 4 TAMA PERAK 31400 IPOH ERAK",
        "Sex": "LEAKI",
        "Birthday": "",
        "Warn": [],
        "Image": "",
        "AdvancedInfo": "{\"ID\":{\"Confidence\":\"1.0000\"},\"Name\":{\"Confidence\":\"0.9996\"},\"Address\":{\"Confidence\":\"0.9997\"},\"Sex\":{\"Confidence\":\"0.9999\"}}",
        "Type": "MyKad",
        "RequestId": "c969da05-54e3-4d0a-a55d-b3ef90d4ebf5"
    }
}
```

