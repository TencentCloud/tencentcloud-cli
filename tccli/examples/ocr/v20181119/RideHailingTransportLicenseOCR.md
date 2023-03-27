**Example 1: 网约车驾驶证识别示例代码**

网约车驾驶证识别示例代码

Input: 

```
tccli ocr RideHailingTransportLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "OperationLicenseNumber": "",
        "VehicleOwner": "品明铭博盘汽年社赁有限本司",
        "VehicleNumber": "延长民东1116号好世县艳云A8R8211",
        "StartDate": "",
        "EndDate": "",
        "ReleaseDate": "2019",
        "RequestId": "0f70356b-ecc8-40f2-bfba-40050f42bbaa"
    }
}
```

