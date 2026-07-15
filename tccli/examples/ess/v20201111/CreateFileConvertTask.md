**Example 1: word文件转换示例**

适用场景：将docx文件转换为pdf

Input: 

```
tccli ess CreateFileConvertTask --cli-unfold-argument  \
    --ResourceType docx \
    --ResourceName 转换文件名称 \
    --ResourceId yD3JmUUckpe***********OREzv3aWCT \
    --Operator.UserId yDtT9UUckp9***********RvxYJ7r7py
```

Output: 
```
{
    "Response": {
        "TaskId": "2026070*******936482",
        "RequestId": "06dd2333-4f98-4c16-b2fb-d54c3dd070d0"
    }
}
```

