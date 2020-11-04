**Example 1: 创建拨测任务示例(扩展)**



Input: 

```
tccli cat CreateTaskEx --cli-unfold-argument  \
    --CatTypeName http\
    --Period 5\
    --AgentGroupId 1510\
    --Url www.tencent.com\
    --TaskName test_http
```

Output: 
```
{
    "Response": {
        "ResultId": 28330,
        "TaskId": 24454,
        "RequestID": "6de91190-a148-97a4-a935-f44cf51e1d61"
    }
}
```

