**Example 1: 错别字及单词拼写检查**

对于一段中英文混杂文本中的错别字和单词拼写进行检查

Input: 

```
tccli portal CorrectText --cli-unfold-argument  \
    --Text 接口返回检茶,tosql
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Offset": 7,
                "Len": 5,
                "WrongSegment": "tosql",
                "Correct": "tdsql"
            },
            {
                "Offset": 5,
                "Len": 1,
                "WrongSegment": "茶",
                "Correct": "查",
                "Policy": "ZhErrCharacters",
                "PolicyDesc": "错别字"
            }
        ],
        "RequestId": "abc"
    }
}
```

