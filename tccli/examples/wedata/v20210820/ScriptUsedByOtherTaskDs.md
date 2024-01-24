**Example 1: 判断脚本文件是否被任务列表所引用**

判断脚本文件是否被任务列表所引用

Input: 

```
tccli wedata ScriptUsedByOtherTaskDs --cli-unfold-argument  \
    --TaskId abc
```

Output: 
```
{
    "Response": {
        "Data": 1,
        "RequestId": "abc"
    }
}
```

