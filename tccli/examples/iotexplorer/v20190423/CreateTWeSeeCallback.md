**Example 1: 创建 TWeSee 回调目标**

创建 HTTP 回调目标

Input: 

```
tccli iotexplorer CreateTWeSeeCallback --cli-unfold-argument  \
    --Type http \
    --CallbackUrl https://example.qq.com/twesee-callback \
    --CallbackToken your-token-here
```

Output: 
```
{
    "Response": {
        "CallbackId": "callback-iak6g98u",
        "RequestId": "f81b1003-d7e9-4899-9f72-4c6d4f6b4f78"
    }
}
```

