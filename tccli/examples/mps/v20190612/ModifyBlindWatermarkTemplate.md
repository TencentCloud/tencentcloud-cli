**Example 1: 修改数字水印模板**

修改数字水印模板

Input: 

```
tccli mps ModifyBlindWatermarkTemplate --cli-unfold-argument  \
    --Definition 10 \
    --Name 数字水印模板2 \
    --Comment 数字水印2 \
    --TextContent 数字水印文字内容2
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

