**Example 1: 语种识别调用示例**

语种识别

Input: 

```
tccli tmt LanguageDetect --cli-unfold-argument  \
    --Text 你好 \
    --ProjectId 0
```

Output: 
```
{
    "Response": {
        "Lang": "zh",
        "RequestId": "155a6879-2c39-4e36-b79c-50a68d073ffc"
    }
}
```

