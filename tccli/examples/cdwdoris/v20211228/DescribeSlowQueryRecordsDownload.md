**Example 1: DescribeSlowQueryRecordsDownload**

下载慢查询文件

Input: 

```
tccli cdwdoris DescribeSlowQueryRecordsDownload --cli-unfold-argument  \
    --InstanceId cdwdoris-3lnbut3w \
    --QueryDurationMs 3000 \
    --EndTime 2025-01-03 15:13:48 \
    --StartTime 2025-01-03 14:58:48 \
    --IsQuery -1
```

Output: 
```
{
    "Response": {
        "CosUrl": "http://cos.test-ap-guangzhou.com",
        "RequestId": "asdfas-xadsfa-adssfad-1sdsa"
    }
}
```

