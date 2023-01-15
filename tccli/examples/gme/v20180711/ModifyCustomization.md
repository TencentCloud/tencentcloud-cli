**Example 1: 修改热句模型**

用户通过该接口可以更新语音消息转文本热句模型。

Input: 

```
tccli gme ModifyCustomization --cli-unfold-argument  \
    --TextUrl https://gme-xxx.cos.xxx.com/customization/1400000000/1400000000_customization \
    --BizId 1400000000 \
    --ModelId 5100f4d60xxx11ed8d6a62xxxeb5fd43
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "RequestId": "29d0ba30-26f9-4f83-9f13-628ed30a824a",
        "ModelId": "5100f4d60xxx11ed8d6a62xxxeb5fd43"
    }
}
```

