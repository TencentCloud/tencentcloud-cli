**Example 1: 泰国身份证识别示例代码**



Input: 

```
tccli ocr RecognizeThaiIDCardOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "ID": "3102001968756",
        "ThaiName": "นาย ธนกฤต  บุญโญปกรุณ์",
        "EnFirstName": "Mr. Thanakit",
        "EnLastName": "Boonyopakron",
        "Address": "ที่อยู่21/19หมู่ที่3ต.บางคูครัดอ.บางบัวทอง",
        "Birthday": "14ธ.ค.2509",
        "IssueDate": "9ธ.ค.2559",
        "ExpirationDate": "13ธ.ค.2567",
        "RequestId": "98f8fcbf-933a-4e95-ac48-6f1a9308fs51"
    }
}
```

