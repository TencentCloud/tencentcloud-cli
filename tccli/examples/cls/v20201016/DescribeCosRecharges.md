**Example 1: 获取cos导入配置**

获取cos导入配置

Input: 

```
tccli cls DescribeCosRecharges --cli-unfold-argument  \
    --TopicId xxx-xxx-xxx-xxx \
    --Status 0 \
    --Enable 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Status": 3,
                "TopicId": "5590efdf-cae5-4703-8d00-2a813xxxxx",
                "BucketRegion": "ap-guangzhou",
                "Enable": 1,
                "Name": "test",
                "Progress": 1,
                "Compress": "gzip",
                "Bucket": "xxxxx-1254xxxx",
                "UpdateTime": "2023-03-08 14:51:14",
                "Id": "0333114e-2e93-42d8-8a2f-a55de8474",
                "LogType": "minimalist_log",
                "Prefix": "xxx/2023/03/07/16/202303071600_000_1030.gz",
                "LogsetId": "03efb75a-0f89-41b0-8cc6-9049a51fexxxx",
                "CreateTime": "2023-03-08 15:29:55",
                "ExtractRuleInfo": {
                    "LogRegex": "",
                    "Keys": [
                        "@time"
                    ],
                    "TimeKey": "",
                    "BeginRegex": "",
                    "UnMatchUpLoadSwitch": true,
                    "Delimiter": ",",
                    "TimeFormat": "",
                    "UnMatchLogKey": "fieldName",
                    "Backtracking": 0
                }
            }
        ],
        "RequestId": "xx-xx-xx-xx"
    }
}
```

