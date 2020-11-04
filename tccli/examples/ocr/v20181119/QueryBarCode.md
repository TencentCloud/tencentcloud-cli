**Example 1: 查询条码信息**

查询条码信息

Input: 

```
tccli ocr QueryBarCode --cli-unfold-argument  \
    --BarCode xxx
```

Output: 
```
{
    "Response": {
        "BarCode": "06941858722888",
        "ProductDataRecords": [
            {
                "ProductName": "真快洁涂擦式清洁剂",
                "EnName": "N.F Inunction Detergent",
                "CategoryCode": "47131830",
                "BrandName": "RQC",
                "Type": "125ML",
                "Width": "180.000",
                "Height": "250.000",
                "Depth": "60.000",
                "KeyWord": "安全真快洁",
                "Description": "专利设计突破原有清洁剂的使用方",
                "ImageLink": [
                    "http://www.anccnet.com/userfile/2011219/137935376.jpg"
                ],
                "ManufacturerName": "深圳市绿韵纳米清洁用品有限公司",
                "ManufacturerAddress": "深圳市坪山新区坑梓街道宝红路12号宝红工业园A栋302",
                "FirmCode": "91440300793853037W",
                "CheckResult": "1"
            }
        ],
        "RequestId": "bc42c967-4810-49fc-b37f-048bbad6965f"
    }
}
```

