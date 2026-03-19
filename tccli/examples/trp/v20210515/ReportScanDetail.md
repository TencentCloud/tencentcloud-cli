**Example 1: 请求示例**



Input: 

```
tccli trp ReportScanDetail --cli-unfold-argument  \
    --ScanDetails.0.Uid 1 \
    --ScanDetails.0.Time 20260317090809 \
    --ScanDetails.0.ProvinceName 湖北 \
    --ScanDetails.0.CityName 武汉 \
    --ScanDetails.0.RegionName 洪山区 \
    --ScanDetails.0.BrandName 品牌2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Count": 1
        },
        "RequestId": "fc2e4ade-956e-4c9c-91bc-d47b417a59bf"
    }
}
```

