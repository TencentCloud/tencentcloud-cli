**Example 1: 创建语音消息转文本热句模型**

用户使用该接口可以创建语音消息转文本热句模型，以供识别调用

Input: 

```
tccli gme CreateCustomization --cli-unfold-argument  \
    --BizId 1400000000 \
    --TextUrl https://gme-xxx.cos.xxx.com/customization/1400000000/1400000000_customization
```

Output: 
```
{
    "Response": {
        "RequestId": "f1338576-0231-4a4b-b441-a780e6ffe894",
        "ModelId": "5100f4d60xxx11ed8d6a62xxxeb5fd43"
    }
}
```

