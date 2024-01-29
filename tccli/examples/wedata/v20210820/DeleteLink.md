**Example 1: 删除连接**

删除连接

Input: 

```
tccli wedata DeleteLink --cli-unfold-argument  \
    --ProjectId abc \
    --TaskFrom abc \
    --TaskTo abc \
    --WorkflowId abc \
    --Id abc
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "abc"
    }
}
```

