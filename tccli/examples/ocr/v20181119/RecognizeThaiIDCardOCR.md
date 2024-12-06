**Example 1: RecognizeThaiIDCardOCR调用**



Input: 

```
tccli ocr RecognizeThaiIDCardOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg
```

Output: 
```
{
    "Response": {
        "Address": "ที่อยู่ 21/19 หมู่ที่ 3 ต.บางคูรัด อ.บางบัวทอง จ.นนทบุรี",
        "AdvancedInfo": "{\"ID\":0.9995814561843872,\"ThaiName\":0.9961479902267456,\"EnFirstName\":0.9232422113418579,\"EnLastName\":0.943652331829071,\"Birthday\":0.9828404188156128,\"EnBirthday\":0.92333984375,\"Religion\":1,\"ExpirationDate\":0.9919084906578064,\"IssueDate\":0.9893275499343872,\"EnExpirationDate\":0.9890950322151184,\"EnIssueDate\":0.9800618290901184,\"SerialNumber\":0.9995659589767456}",
        "Birthday": "14 ธ.ค. 2509",
        "EnBirthday": "14 Dec. 1966",
        "EnExpirationDate": "13 Dec. 2024",
        "EnFirstName": "Mr. Thanakit",
        "EnIssueDate": "9 Dec. 2016",
        "EnLastName": "Boonyopakron",
        "ExpirationDate": "13 ธ.ค. 2567",
        "ID": "3 1020 01968 75 6",
        "IssueDate": "9 ธ.ค. 2559",
        "PortraitImage": "",
        "Religion": "พุทธ",
        "RequestId": "d4af8019-08e0-4d8d-a986-e1f45efb4a6c",
        "SerialNumber": "1204-03-12091012",
        "ThaiName": "นาย ธนกฤต บุญโญปกรณ์",
        "WarnCardInfos": [
            -9109
        ]
    }
}
```

