**Example 1: 资源管理-判断资源文件是否存在**

判断资源文件是否存在

Input: 

```
tccli wedata JudgeResourceFile --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --FilePath a/b
```

Output: 
```
{
    "Response": {
        "Data": "ab/c",
        "RequestId": "3b4d1a5a-69bf-41c7-946c-dd609cf89119"
    }
}
```

