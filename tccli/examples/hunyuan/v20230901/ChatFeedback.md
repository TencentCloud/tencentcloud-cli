**Example 1: 反馈成功**

反馈成功

Input: 

```
tccli hunyuan ChatFeedback --cli-unfold-argument  \
    --ReqId c8cce39c-9d06-4a95-8f41-84044d28c59d \
    --Rate 10 \
    --Feedback 效果不错
```

Output: 
```
{
    "Response": {
        "RequestId": "450fb6a1-0cd3-4d2a-8038-db0443c22021"
    }
}
```

**Example 2: 请求失败**

任务不存在

Input: 

```
tccli hunyuan ChatFeedback --cli-unfold-argument  \
    --ReqId 26e63394-8045-4afa-b624-f5c1f752acae呃问我 \
    --Rate 1 \
    --Feedback 12434343434
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.NoSuchRequest",
            "Message": ""
        },
        "RequestId": "6710ff5f-45dc-494b-bf9e-915e3134c071"
    }
}
```

