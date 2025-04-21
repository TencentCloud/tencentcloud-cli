**Example 1: 日志下载**

日志下载

Input: 

```
tccli ioa DescribeLogDownloadURL --cli-unfold-argument  \
    --Sort.Field abc \
    --Sort.Order abc \
    --UserName abc \
    --StartTime 0 \
    --LogId abc \
    --Department 0 \
    --LogDownloadFields abc \
    --EndpointGroup 0 \
    --Filters.0.Field abc \
    --Filters.0.Operator abc \
    --Filters.0.Values abc \
    --Filters.0.Describe abc \
    --OsType 0 \
    --EndTime 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownloadURL": "abc",
            "DownloadToken": "abc",
            "ExpireAt": "abc"
        },
        "RequestId": "abc"
    }
}
```

