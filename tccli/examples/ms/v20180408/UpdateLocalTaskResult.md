**Example 1: 结果上报**

结果上报

Input: 

```
tccli ms UpdateLocalTaskResult --cli-unfold-argument  \
    --Sid Sid-xxxxx \
    --ResultCode 0 \
    --SubCode 0 \
    --ErrMsg success \
    --Result result_info
```

Output: 
```
{
    "Response": {
        "ResultCode": "1",
        "RequestId": "RequestId-xxxxx"
    }
}
```

