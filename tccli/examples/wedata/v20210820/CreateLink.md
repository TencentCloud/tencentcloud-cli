**Example 1: 创建任务连接**

工作流画布-创建任务连接

Input: 

```
tccli wedata CreateLink --cli-unfold-argument  \
    --ProjectId abc \
    --TaskFrom abc \
    --TaskTo abc \
    --WorkflowId abc
```

Output: 
```
{
    "Response": {
        "Data": "abc",
        "RequestId": "abc"
    }
}
```

