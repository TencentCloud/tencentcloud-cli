**Example 1: 查询提示词模板标签列表**



Input: 

```
tccli adp DescribePromptTemplateLabelList --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 10 \
    --Query 通用
```

Output: 
```
{
    "Response": {
        "PromptTemplateLabelList": [
            {
                "Content": "通用提示词",
                "PromptTemplateLabelId": "1957634992069301385",
                "PromptTemplateLabelType": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "4e79f459-175b-434a-b6ce-7de33665af1a"
    }
}
```

