**Example 1: 查询应用资源配置**



Input: 

```
tccli tiw DescribeWhiteboardApplicationConfig --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --TaskTypes transcode recording
```

Output: 
```
{
    "Response": {
        "Configs": [
            {
                "BucketLocation": "ap-nanjing",
                "BucketName": "example-120000001",
                "BucketPrefix": "video",
                "Callback": "http://www.test.com",
                "CallbackKey": "",
                "ResultDomain": "example-120000001.cos.ap-nanjing.myqcloud.com",
                "TaskType": "recording",
                "SdkAppId": 1400127140
            },
            {
                "BucketLocation": "ap-nanjing",
                "BucketName": "example-120000001",
                "BucketPrefix": "",
                "Callback": "http://www.test.com/qcapi",
                "CallbackKey": "abcde",
                "ResultDomain": "example-120000001.cos.ap-nanjing.myqcloud.com",
                "TaskType": "transcode",
                "SdkAppId": 1400127140
            }
        ],
        "SdkAppId": 1400127140,
        "RequestId": "9f5a59d6-2b77-41b2-a945-78084577e225"
    }
}
```

