**Example 1: 修改 TWeSee 回调目标**

修改指定回调目标

Input: 

```
tccli iotexplorer ModifyTWeSeeCallback --cli-unfold-argument  \
    --CallbackId callback-iak6g98u \
    --Type http \
    --CallbackUrl https://example.qq.com/twesee-callback?v=2 \
    --CallbackToken token-456
```

Output: 
```
{
    "Response": {
        "RequestId": "07e32598-feb4-45ee-b0bf-fcc67ef0ec1a"
    }
}
```

