**Example 1: 成功**

成功

Input: 

```
tccli wedata CreateTaskDs --cli-unfold-argument  \
    --ProjectId abc \
    --WorkflowId abc \
    --TaskName abc \
    --TaskType 0 \
    --TaskExt.0.Key abc \
    --TaskExt.0.Value abc
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

**Example 2: 成功示例**

成功示例

Input: 

```
tccli wedata CreateTaskDs --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --WorkflowId e36dadbf-ebb3-11ed-8909-bc97e105ba60 \
    --TaskName quinncreate0717 \
    --TaskType 26
```

Output: 
```
{
    "Response": {
        "Data": "20230717143540689",
        "RequestId": "9fbc5257-68ee-4225-9959-6ff0a93dd2eb"
    }
}
```

