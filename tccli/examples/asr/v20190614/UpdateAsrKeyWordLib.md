**Example 1: 更新关键词表**

用户通过该API传入已经创建的关键词表ID，可以更新其相应的内容

Input: 

```
tccli asr UpdateAsrKeyWordLib --cli-unfold-argument  \
    --KeyWordLibId aa6f402f263f12ea856fc81fbecfd0sd \
    --Name 新的词表名称
```

Output: 
```
{
    "Response": {
        "Data": {
            "KeyWordLibId": "aa6f402f263f12ea856fc81fbecfd0sd"
        },
        "RequestId": "3290cfb2-91a7-4989-91de-d1d624a77c12"
    }
}
```

