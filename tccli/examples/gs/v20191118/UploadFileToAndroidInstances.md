**Example 1: 上传文件到安卓实例示例**



Input: 

```
tccli gs UploadFileToAndroidInstances --cli-unfold-argument  \
    --AndroidInstanceIds abc \
    --FileURL http://xxx
```

Output: 
```
{
    "Response": {
        "TaskSet": [
            {
                "TaskId": "abc",
                "AndroidInstanceId": "abc"
            }
        ],
        "RequestId": "af454786-99e1-4fc7-8ffa-2ecef1e69715"
    }
}
```

