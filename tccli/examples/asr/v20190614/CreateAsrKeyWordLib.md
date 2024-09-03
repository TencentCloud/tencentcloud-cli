**Example 1: 创建关键词表**

用户通过上传文件方式创建关键词表

Input: 

```
tccli asr CreateAsrKeyWordLib --cli-unfold-argument  \
    --Name 词表名称 \
    --KeyWordFile <文件base64>
```

Output: 
```
{
    "Response": {
        "Data": {
            "KeyWordLibId": "aa6f402f263f12ea856fc81fbecfd0sd"
        },
        "RequestId": "b3808ad3-d8dd-4b65-96c9-7d6f1f81b6b6"
    }
}
```

