**Example 1: 获取报告分类结果**



Input: 

```
tccli cii DescribeReportClassify --cli-unfold-argument  \
    --ServiceType Structured \
    --FileList 700000198392/original_upload_dir/700000198392_b0a3da0c-af75-464f-b202-f49c7127c012.pdf 700000198392/original_upload_dir/700000198392_6622637e-4da0-11ec-b930-525400f962860_rh95vodxdkw.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "22dfcc05-1ba1-49b4-a751-f5611cdb3420",
        "Reports": [
            {
                "ReportType": "HealthReport",
                "FileList": [
                    "700000198392/original_upload_dir/700000198392_b0a3da0c-af75-464f-b202-f49c7127c012.pdf"
                ]
            },
            {
                "ReportType": "MedCheckReport",
                "FileList": [
                    "700000198392/original_upload_dir/700000198392_6622637e-4da0-11ec-b930-525400f962860_rh95vodxdkw.jpg"
                ]
            }
        ]
    }
}
```

