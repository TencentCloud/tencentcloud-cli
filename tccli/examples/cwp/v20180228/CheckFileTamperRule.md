**Example 1: 示例**



Input: 

```
tccli cwp CheckFileTamperRule --cli-unfold-argument  \
    --Name xx \
    --Id 1
```

Output: 
```
{
    "Response": {
        "RequestId": "d92d723e-4aac-4f4a-bbf9-e5430e29d289",
        "ErrCode": 1,
        "ErrMsg": "规则名称已存在"
    }
}
```

