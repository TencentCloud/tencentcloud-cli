**Example 1: 上传文件到安卓实例示例**



Input: 

```
tccli gs UploadFileToAndroidInstances --cli-unfold-argument  \
    --AndroidInstanceIds cai-abcd1234 \
    --FileURL http://xxx
```

Output: 
```
{
    "Response": {
        "TaskSet": [
            {
                "TaskId": "615cf0a4-075e-4cf5-b26f-d786363daccd",
                "AndroidInstanceId": "cai-abcd1234"
            }
        ],
        "RequestId": "af454786-99e1-4fc7-8ffa-2ecef1e69715"
    }
}
```

