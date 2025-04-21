**Example 1: 创建日志下载任务**

创建日志下载任务

Input: 

```
tccli ioa CreateLogDownloadTask --cli-unfold-argument  \
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
            "Message": "abc"
        },
        "RequestId": "abc"
    }
}
```

