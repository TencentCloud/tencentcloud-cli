**Example 1: 查询用户自定义数字水印模板**

查询用户自定义数字水印模板

Input: 

```
tccli mps DescribeBlindWatermarkTemplates --cli-unfold-argument  \
    --Definitions 10 20 30 \
    --Type blind-basic \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "BlindWatermarkTemplateSet": [
            {
                "Definition": 1001,
                "Type": "blind-basic",
                "Name": "数字水印模板1",
                "Comment": "测试模板",
                "TextContent": "文字内容",
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z"
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

