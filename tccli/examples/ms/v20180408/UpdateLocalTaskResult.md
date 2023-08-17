**Example 1: 结果上报**

结果上报

Input: 

```
tccli ms UpdateLocalTaskResult --cli-unfold-argument  \
    --Sid abc \
    --ResultCode 0 \
    --SubCode 0 \
    --ErrMsg abc \
    --Result abc
```

Output: 
```
{
    "Response": {
        "ResultCode": "abc",
        "RequestId": "abc"
    }
}
```

