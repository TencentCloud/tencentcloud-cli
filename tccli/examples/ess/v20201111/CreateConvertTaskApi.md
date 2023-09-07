**Example 1: jpg文件转换示例**

适用场景：将jpg文件转换为pdf

Input: 

```
tccli ess CreateConvertTaskApi --cli-unfold-argument  \
    --ResourceType jpg \
    --ResourceName 合同图片.jpg \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --ResourceId yDRSRUUgygj6qnwfUuO4zjEwc193c2hH
```

Output: 
```
{
    "Response": {
        "RequestId": "d245a68d-e13b-xxxx-xxxx-e5adc794db24",
        "TaskId": "202xxxx3011294"
    }
}
```

**Example 2: word文件转换示例**

适用场景：将docx文件转换为pdf

Input: 

```
tccli ess CreateConvertTaskApi --cli-unfold-argument  \
    --ResourceType docx \
    --ResourceName 员工劳动合同.docx \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --ResourceId yDRSRUUgygj6qnyvUuO4zjE1vLuGdWjL
```

Output: 
```
{
    "Response": {
        "RequestId": "d245a68d-e13b-xxxx-xxxx-e5adc794db24",
        "TaskId": "20220xxxx549202141"
    }
}
```

