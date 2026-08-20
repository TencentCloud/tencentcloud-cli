**Example 1: 获取镜像聚合信息**



Input: 

```
tccli tke DescribeOSImages --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "OSImageSeriesSet": [
            {
                "Alias": "TencentOS Server 2.4 (TK4) HCC",
                "Arch": "amd64",
                "ImageId": "img-nannz3uj",
                "OsCustomizeType": "GENERAL",
                "OsName": "tlinux2.4(tkernel4)x86_64_HCC",
                "SeriesName": "TencentOS Server 2.4 (TK4) HCC",
                "Status": "online"
            }
        ],
        "TotalCount": 17,
        "RequestId": "72c5ebe4-166f-40a2-95b1-d3e9dfcdd5da"
    }
}
```

