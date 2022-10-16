**Example 1: 成功示例**



Input: 

```
tccli faceid CreateUploadUrl --cli-unfold-argument  \
    --TargetAction ApplyWebVerificationToken
```

Output: 
```
{
    "Response": {
        "ExpiredTimestamp": 1637212877,
        "RequestId": "2e546a7c-4e12-43f6-bf98-d33d3724ea5b",
        "ResourceUrl": "https://singapore-1257237511.cos.ap-singapore.myqcloud.com/faceid%2FApplyWebVerificationToken%2F2e546a7c-4e12-43f6-bf98-d33d3724ea5b?q-sign-algorithm=sha1&q-ak=AKIDeQ4Zsyob70ywoF8ijZDj5IJ8bzBHfuQk&q-sign-time=1637205677%3B1637212877&q-key-time=1637205677%3B1637212877&q-header-list=host&q-url-param-list=&q-signature=32302bad71219f9ebcae6f4703ae05b0ae33378f",
        "UploadUrl": "https://singapore-1257237511.cos.ap-singapore.myqcloud.com/faceid%2FApplyWebVerificationToken%2F2e546a7c-4e12-43f6-bf98-d33d3724ea5b?q-sign-algorithm=sha1&q-ak=AKIDeQ4Zsyob70ywoF8ijZDj5IJ8bzBHfuQk&q-sign-time=1637205677%3B1637212877&q-key-time=1637205677%3B1637212877&q-header-list=host&q-url-param-list=&q-signature=9495ea0b69a2b2fb6b53a0e8d8a0dcd836762bbd"
    }
}
```

