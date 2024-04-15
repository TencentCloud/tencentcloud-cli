**Example 1: 获取文档下拉列表**

获取文档下拉列表

Input: 

```
tccli lke ListSelectDoc --cli-unfold-argument  \
    --BotBizId 1714970520775950336 \
    --FileName 26
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Text": "26种病虫害防治方法.docx",
                "Value": "630"
            }
        ],
        "RequestId": "0b598870-f2e7-4fcc-ada0-7cf99a8fbc8e"
    }
}
```

