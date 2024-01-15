**Example 1: 外国人永久居留身份证识别**

外国人永久居留身份证识别

Input: 

```
tccli ocr RecognizeForeignPermanentResidentIdCard --cli-unfold-argument  \
    --ImageUrl abc \
    --ImageBase64 abc \
    --EnablePdf True \
    --PdfPageNumber 1
```

Output: 
```
{
    "Response": {
        "CnName": "abc",
        "EnName": "abc",
        "Sex": "abc",
        "DateOfBirth": "abc",
        "Nationality": "abc",
        "PeriodOfValidity": "abc",
        "No": "abc",
        "RequestId": "abc"
    }
}
```

