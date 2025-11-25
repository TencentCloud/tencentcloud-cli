**Example 1: 创建数字水印模板**

创建数字水印模板

Input: 

```
tccli mps CreateBlindWatermarkTemplate --cli-unfold-argument  \
    --Name 数字水印模板1 \
    --Comment 数字水印 \
    --Type blind-nagra \
    --TextContent 数字水印文字
```

Output: 
```
{
    "Response": {
        "Definition": 10,
        "RequestId": "93dda61a-c2c5-465d-a78c-0860997fb01b"
    }
}
```

