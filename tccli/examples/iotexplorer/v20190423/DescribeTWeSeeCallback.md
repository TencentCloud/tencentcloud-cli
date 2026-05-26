**Example 1: 查询 TWeSee 回调目标详情**

查询指定回调目标详情

Input: 

```
tccli iotexplorer DescribeTWeSeeCallback --cli-unfold-argument  \
    --CallbackId callback-iak6g98u
```

Output: 
```
{
    "Response": {
        "CallbackInfo": {
            "CallbackId": "callback-iak6g98u",
            "Type": "http",
            "CallbackUrl": "https://example.qq.com/twesee-callback",
            "CallbackToken": "your-token-here",
            "CreateTime": 1738827748,
            "UpdateTime": 1738827789
        },
        "RequestId": "72f3139f-21a8-4f20-8f7d-f5f95022b9eb"
    }
}
```

