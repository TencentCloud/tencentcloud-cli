**Example 1: 1**

1

Input: 

```
tccli wedata BatchDeleteOpsTasks --cli-unfold-argument  \
    --TaskIdList abc \
    --DeleteMode True \
    --EnableNotify True \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "SuccessCount": 0,
            "FailedCount": 0,
            "TotalCount": 0
        },
        "RequestId": "abc"
    }
}
```

**Example 2: 123**

456

Input: 

```
tccli wedata BatchDeleteOpsTasks --cli-unfold-argument  \
    --TaskIdList 123 \
    --DeleteMode True \
    --EnableNotify True \
    --ProjectId 123
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "An internal error has occurred. Retry your request, but if the problem persists, contact us."
        },
        "RequestId": "188b3e3b-90a4-4e53-a01f-16046dda13f6"
    }
}
```

**Example 3: hello**

hi

Input: 

```
tccli wedata BatchDeleteOpsTasks --cli-unfold-argument  \
    --TaskIdList 2 \
    --DeleteMode True \
    --EnableNotify True \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "An internal error has occurred. Retry your request, but if the problem persists, contact us."
        },
        "RequestId": "1d510800-9cd8-41ee-84e0-04bbd8cecc81"
    }
}
```

**Example 4: 失败实例**

失败实例

Input: 

```
tccli wedata BatchDeleteOpsTasks --cli-unfold-argument  \
    --TaskIdList abc \
    --DeleteMode True \
    --EnableNotify True \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "An internal error has occurred. Retry your request, but if the problem persists, contact us."
        },
        "RequestId": "1d287884-1214-4b75-b4e8-383ee8e57918"
    }
}
```

