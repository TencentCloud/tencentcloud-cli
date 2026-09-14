**Example 1: RecognizeThaiIDCardOCR调用**



Input: 

```
tccli ocr RecognizeThaiIDCardOCR --cli-unfold-argument  \
    --ImageUrl https://ai-demo-1426683817.cos.ap-chengdu.myqcloud.com/xxx
```

Output: 
```
{
    "Response": {
        "Address": "ที่อยู่ 27 ****ฐีระเวช 7 ต.ตะพ***ิน ****พานห** จ.พิจิตร",
        "Birthday": "28 ม.ค. 2542",
        "EnBirthday": "28 Jan. 1999",
        "EnExpirationDate": "27 Jan. 2031",
        "EnFirstName": "Miss Nat*****cha",
        "EnIssueDate": "26 Mar. 2022",
        "EnLastName": "Ph*******wan",
        "ExpirationDate": "27 ม.ค. 2574",
        "ID": "1 6604 ***** 52 4",
        "IssueDate": "26 มี.ค. 2565",
        "LaserID": "",
        "PortraitImage": "",
        "Religion": "พุทธ",
        "SerialNumber": "10**-03-*****113",
        "ThaiName": "น.ส. ณั*********ชราวรรณ",
        "WarnCardInfos": [
            -9109
        ],
        "RequestId": "23e58a98-0cbd-46dd-aad8-7144bf7cf47a"
    }
}
```

