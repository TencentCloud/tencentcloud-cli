**Example 1: 申请成功**



Input: 

```
tccli faceid ApplyWebVerificationToken --cli-unfold-argument  \
    --RedirectUrl https://www.domain.com/result/callback \
    --CompareImageUrl https%3A%2F%2Fsingapore-1257237511.cos.ap-singapore.myqcloud.com%2Ffaceid%2F%2Ftest.png%3Fq-sign-algorithm%3Dsha1%26q-ak%3DAKIDpguZTmihib_W5VoMU1T07CvytjqfY6auKJN6akSM4tmgbmjHnwl2d7EW9TIUYxmK%26q-sign-time%3D1637288206%3B1637291806%26q-key-time%3D1637288206%3B1637291806%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D7b95d6494e30b05c493ea32db18bbded2e52cd20%26x-cos-security-token%3DkdihJH25E3bZ062DmV2DK1Hv7kE9LQgab4e9fcd283fe59181502e2e1cbecca83iCHquGrh0AClApqec56ahy-298Taz8DrfmRBHFlARDI1XytSLuMcSltSighEh-N7hRDmcug2POunRzWY5JIi7vYiSTxDj1QDZql5o1C6nraxlGkyM-EAZquEK1M6hUXFV6x1_C1G0CpUi3-TJl0cx5M1MUItmdx0h3vZ9u0IuEtZgrvGDrEAViW432lRrlSi \
    --CompareImageMd5 2455b660dfe11f7e00ddf4831603d897
```

Output: 
```
{
    "Response": {
        "BizToken": "0AEEA2AE-7166-4EA4-BD82-3494ECF216BD",
        "RequestId": "f3ef2ddf-c5a6-4e2a-9ac6-441231ba8a61",
        "VerificationUrl": "https://sg.faceid.qq.com/reflect/?token=0AEEA2AE-7166-4EA4-BD82-3494ECF216BD"
    }
}
```

