**Example 1: 正常响应**



Input: 

```
tccli faceid ApplyCardVerification --cli-unfold-argument  \
    --ImageUrlFront https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg \
    --ImageUrlBack https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg \
    --Nationality HKG \
    --CardType ID_CARD
```

Output: 
```
{
    "Response": {
        "CardVerificationToken": "b607d0ad-edca-4b54-a35d-b72ef254dc11",
        "AsyncCardVerificationMaxPollingTimes": 60,
        "AsyncCardVerificationPollingWaitTime": 5,
        "RequestId": "a498a726-9596-467c-88dc-c68ba51ab4c8"
    }
}
```

