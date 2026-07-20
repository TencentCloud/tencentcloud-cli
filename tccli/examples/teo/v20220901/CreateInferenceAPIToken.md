**Example 1: 创建推理 API Token**

创建指定名称的推理 API Token。

Input: 

```
tccli teo CreateInferenceAPIToken --cli-unfold-argument  \
    --ZoneId zone-2***8ev000 \
    --Name MyInferenceAPIToken
```

Output: 
```
{
    "Response": {
        "Content": "j8UaDh0ZbjW***glcGsSEEYo",
        "TokenId": "deb88f89-92b***3f3466bbb59b",
        "RequestId": "38b7c3a3-82ac-47ad-aa01-712414ef9eaf"
    }
}
```

