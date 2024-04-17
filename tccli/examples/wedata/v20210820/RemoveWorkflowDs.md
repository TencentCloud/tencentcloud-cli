**Example 1: 示例1**

demo

Input: 

```
tccli wedata RemoveWorkflowDs --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --WorkflowId a09dac50-ed66-11ed-8909-bc97e105ba60
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "534ab7ba-7399-4dc7-b45d-9721e3aff985"
    }
}
```

**Example 2: 工作流不存在**

失败示例1

Input: 

```
tccli wedata RemoveWorkflowDs --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --WorkflowId a09dac50-ed66-11ed-8909-bc97e105ba60
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "要删除的工作流不存在"
        },
        "RequestId": "9849acb3-fde9-4c6e-806c-9230fe4ccf01"
    }
}
```

