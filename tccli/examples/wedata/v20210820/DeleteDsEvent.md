**Example 1: 批量删除事件**

批量删除事件

Input: 

```
tccli wedata DeleteDsEvent --cli-unfold-argument  \
    --ProjectId abc \
    --EventNameSet abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 0,
            "SuccessCount": 0,
            "FailCount": 0,
            "FailMessageList": [
                {
                    "Key": "abc",
                    "ErrorMessage": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

