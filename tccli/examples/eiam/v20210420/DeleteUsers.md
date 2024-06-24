**Example 1: 请求示例**



Input: 

```
tccli eiam DeleteUsers --cli-unfold-argument  \
    --DeleteIdList uid222222 \
    --DeleteNameList 用户22222
```

Output: 
```
{
    "Response": {
        "RequestId": "requestId22222",
        "FailedItems": [
            "uid2222222"
        ]
    }
}
```

