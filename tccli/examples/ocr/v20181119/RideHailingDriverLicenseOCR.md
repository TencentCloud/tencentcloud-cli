**Example 1: 网约车驾驶证识别示例代码**

网约车驾驶证识别示例代码

Input: 

```
tccli ocr RideHailingDriverLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg
```

Output: 
```
{
    "Response": {
        "Name": "张**",
        "LicenseNumber": "130****13",
        "StartDate": "20190925",
        "EndDate": "20190925",
        "ReleaseDate": "20190925",
        "RequestId": "aa534793deqd1dqq948487"
    }
}
```

