**Example 1: DescribeSlowQueryRecordsDownload**

下载慢查询文件

Input: 

```
tccli cdwdoris DescribeSlowQueryRecordsDownload --cli-unfold-argument  \
    --InstanceId abc \
    --QueryDurationMs 0 \
    --StartTime abc \
    --EndTime abc \
    --DurationMs abc
```

Output: 
```
{
    "Response": {
        "CosUrl": "abc",
        "RequestId": "abc"
    }
}
```

