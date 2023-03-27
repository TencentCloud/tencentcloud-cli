**Example 1: 网约车驾驶证识别示例代码**

网约车驾驶证识别示例代码

Input: 

```
tccli ocr RideHailingDriverLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Name": "张市学",
        "LicenseNumber": "130622196402222413",
        "StartDate": "20190925",
        "EndDate": "",
        "ReleaseDate": "20190925",
        "RequestId": "aa534793deqd1dqq948487"
    }
}
```

