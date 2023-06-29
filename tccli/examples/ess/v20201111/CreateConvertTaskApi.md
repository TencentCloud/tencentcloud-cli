**Example 1: 调用示例**

适用场景：通过word文件资源id进行文件转换

Input: 

```
tccli ess CreateConvertTaskApi --cli-unfold-argument  \
    --ResourceType doc \
    --ResourceId y***********************************l \
    --Operator.UserId y***********************************p \
    --ResourceName hello.docx
```

Output: 
```
{
    "Response": {
        "RequestId": "b2eae8xxxx61cfaf19a21",
        "TaskId": "202xxxx3011294"
    }
}
```

**Example 2: test示例**

适用场景：通过word文件资源id进行文件转换

Input: 

```
tccli ess CreateConvertTaskApi --cli-unfold-argument  \
    --ResourceType doc \
    --ResourceName hello.docx \
    --Operator.UserId y***********************************R \
    --ResourceId y***********************************l
```

Output: 
```
{
    "Response": {
        "RequestId": "fbf25f31-xxxxxfed19e9849",
        "TaskId": "20220xxxx549202141"
    }
}
```

