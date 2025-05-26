**Example 1: 成功示例**

成功示例

Input: 

```
tccli ca DescribeFileUploadUrl --cli-unfold-argument  \
    --Types pdf
```

Output: 
```
{
    "Response": {
        "Keys": [
            "2300001383-11f7b07e-2b34-4bae-ae94-318ba1f7c2ff0.pdf"
        ],
        "RequestId": "11f7b07e-2b34-4bae-ae94-318ba1f7c2ff",
        "StatusCode": 1,
        "Urls": [
            "https://approvals-1312375811.cos.ap-shanghai.myqcloud.com/2300001383-11f7b07e-2b34-4bae-ae94-318ba1f7c2ff0.pdf?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDJRIzPZS3NQChwub1A2dx0mHVR6UcT2KM%26q-sign-time%3D1681991977%3B1681992337%26q-key-time%3D1681991977%3B1681992337%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D780532a0b933a66f6700d9b79617972fb6c8d987"
        ]
    }
}
```

