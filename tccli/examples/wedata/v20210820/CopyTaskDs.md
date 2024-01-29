**Example 1: 失败**

失败

Input: 

```
tccli wedata CopyTaskDs --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --TaskId 20230516193558842 \
    --TaskName quinnz \
    --WorkflowId e36dadbf-ebb3-11ed-8909-bc97e105ba60
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "create task quinnz Exception"
        },
        "RequestId": "ebc9c273-32f0-4637-b83c-0da6f9046756"
    }
}
```

**Example 2: 成功**

成功

Input: 

```
tccli wedata CopyTaskDs --cli-unfold-argument  \
    --ProjectId abc \
    --TaskId abc \
    --TaskName abc \
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

