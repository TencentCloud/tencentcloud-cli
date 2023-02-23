**Example 1: 查询条码信息**

查询条码信息

Input: 

```
tccli ocr QueryBarCode --cli-unfold-argument  \
    --BarCode 6928804021912
```

Output: 
```
{
    "Response": {
        "BarCode": "06928804021912",
        "ProductDataRecords": [
            {
                "BrandName": "美汁源",
                "CategoryCode": "",
                "CheckResult": "1",
                "Depth": "",
                "Description": "",
                "EnName": "",
                "FirmCode": "911100006000138767",
                "Height": "",
                "ImageLink": [
                    ""
                ],
                "KeyWord": "480ml美汁源葡萄气泡饮葡萄汁汽水 *12",
                "ManufacturerAddress": "北京市朝阳区酒仙桥路20号楼3层301号312室",
                "ManufacturerName": "太古中萃发展有限公司",
                "ProductName": "480ml美汁源葡萄气泡饮葡萄汁汽水 *12",
                "Type": "480ml*12",
                "Width": ""
            }
        ],
        "RequestId": "e2ca3708-f5cd-49de-b254-4d9beca0eef6"
    }
}
```

