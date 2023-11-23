**Example 1: 调用接口成功案例**



Input: 

```
tccli hunyuan GetTokenCount --cli-unfold-argument  \
    --Prompt 你是谁
```

Output: 
```
{
    "Response": {
        "RequestId": "c9e24deb-dd6d-4fe5-b0ca-c9292d1f1a9d",
        "TokenCount": 2,
        "CharacterCount": 3,
        "Tokens": [
            "你是",
            "谁"
        ]
    }
}
```

