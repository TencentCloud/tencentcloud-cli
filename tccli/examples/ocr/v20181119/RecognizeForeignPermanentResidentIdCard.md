**Example 1: 外国人永久居留身份证识别**

外国人永久居留身份证识别

Input: 

```
tccli ocr RecognizeForeignPermanentResidentIdCard --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/ForeignPermanentResidentIdCard/ForeignPermanentResidentIdCard1.jpg \
    --ImageBase64 /9j/4AAQSkZJRg.....s97n//2Q== \
    --EnablePdf True \
    --PdfPageNumber 1
```

Output: 
```
{
    "Response": {
        "CnName": "吴全斌",
        "EnName": "QUANBIN,WU",
        "Sex": "男/M",
        "DateOfBirth": "1981年08月03日",
        "Nationality": "加拿大/CAN",
        "PeriodOfValidity": "自2023年09月15日至2033年09月14日",
        "No": "911124198108030024",
        "RequestId": "a39aa7d9-2e31-463e-b3c9-7894ca53c729"
    }
}
```

