**Example 1: 当前支持策略**

纠错系统当前支持的所有检查策略

Input: 

```
tccli portal GetCurrentPolicy --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Instruction": "敏感数据",
                "Policy": "sensitiveNumber",
                "Props": ""
            },
            {
                "Instruction": "错别字",
                "Policy": "zhErrCharacters",
                "Props": "gpt,botong"
            },
            {
                "Instruction": "链接",
                "Policy": "link",
                "Props": ""
            },
            {
                "Instruction": "代码",
                "Policy": "code",
                "Props": "php,go"
            },
            {
                "Instruction": "黑名单检测",
                "Policy": "blackList",
                "Props": ""
            },
            {
                "Instruction": "标点符号",
                "Policy": "symbols",
                "Props": ""
            },
            {
                "Instruction": "单词拼写",
                "Policy": "word",
                "Props": ""
            }
        ],
        "RequestId": "8483c40e-ddb5-4d45-84c2-a36041d14055"
    }
}
```

