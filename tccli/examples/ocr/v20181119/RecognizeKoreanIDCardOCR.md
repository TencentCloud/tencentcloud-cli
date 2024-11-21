**Example 1: 韩国身份证识别**

韩国身份证识别

Input: 

```
tccli ocr RecognizeKoreanIDCardOCR --cli-unfold-argument  \
    --ReturnHeadImage true \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg
```

Output: 
```
{
    "Response": {
        "Address": "서울특별시 종로구은천로 93.1203동 1204호(봉천동, 진달래아파트101동 2301호)",
        "Birthday": "01/07/1982",
        "DateOfIssue": "01/01/8207",
        "ID": "820701-2345678",
        "Name": "홍길동 (洪吉童)",
        "Photo": "/9j/4AAQSkZJRg.....s97n//2Q==",
        "RequestId": "8b03725a-d5b3-4dfa-81b5-55214271a69a",
        "Sex": "女"
    }
}
```

