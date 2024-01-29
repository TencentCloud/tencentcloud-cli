**Example 1: 失败**

失败

Input: 

```
tccli wedata UpdateBatchTaskParams --cli-unfold-argument  \
    --TaskIds 20230608210301228 \
    --MapParamList.0.Key abc \
    --MapParamList.0.Value 123 \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "An internal error has occurred. Retry your request, but if the problem persists, contact us."
        },
        "RequestId": "ce0c961f-24dd-43aa-a5bf-1e0b2c1c6a38"
    }
}
```

**Example 2: 成功**



Input: 

```
tccli wedata UpdateBatchTaskParams --cli-unfold-argument  \
    --TaskIds abc \
    --MapParamList.0.Key abc \
    --MapParamList.0.Value abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": 1
        },
        "RequestId": "abc"
    }
}
```

**Example 3: 成功2**

成功2

Input: 

```
tccli wedata UpdateBatchTaskParams --cli-unfold-argument  \
    --TaskIds 20230804121936196 \
    --MapParamList.0.Key def \
    --MapParamList.0.Value 456 \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": 1
        },
        "RequestId": "abc"
    }
}
```

