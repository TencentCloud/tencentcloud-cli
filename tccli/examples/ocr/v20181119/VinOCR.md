**Example 1: 车辆VIN码识别示例代码**



Input: 

```
tccli ocr VinOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/vehicle/VinOCR/VinOCR1.jpg
```

Output: 
```
{
    "Response": {
        "Vin": "LSGPC52H9GF125161",
        "RequestId": "c59d9002-6c8c-426d-b57f-a8837dee2c7c"
    }
}
```

