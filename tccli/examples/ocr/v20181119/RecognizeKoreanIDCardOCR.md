**Example 1: 韩国驾驶证识别**



Input: 

```
tccli ocr RecognizeKoreanIDCardOCR --cli-unfold-argument  \
    --ReturnHeadImage false \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Address": "서=은천로 93.1203동 1204호(봉천동, 진달01동 2301호)",
        "DateOfIssue": "297802",
        "ID": "",
        "Name": "홍길동(离吉)",
        "Photo": "",
        "Birthday": "11/11/1911",
        "Sex": "",
        "RequestId": "1234-1234-1234-1234"
    }
}
```

