**Example 1: 请求示例**



Input: 

```
tccli clouddc DescribePkgExist --cli-unfold-argument  \
    --TaskId 100000428 \
    --QueryUin 100032961887
```

Output: 
```
{
    "Response": {
        "ExistResult": [
            {
                "Result": 0,
                "TaskId": 100000428
            }
        ],
        "RequestId": "0"
    }
}
```

