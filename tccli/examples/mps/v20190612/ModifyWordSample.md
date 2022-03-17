**Example 1: 修改关键词样本**



Input: 

```
tccli mps ModifyWordSample --cli-unfold-argument  \
    --Keyword 格斗 \
    --Usages Review \
    --TagOperationInfo.Type reset \
    --TagOperationInfo.Tags 敏感信息
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

