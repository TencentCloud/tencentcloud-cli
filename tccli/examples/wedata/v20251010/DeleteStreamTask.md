**Example 1: DeleteStreamTask调用示例**

需要确保task id存在

Input: 

```
tccli wedata DeleteStreamTask --cli-unfold-argument  \
    --WorkspaceId id_1 \
    --TaskId ec438445-aeca-4859-8610-05e83ba6dc06
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": true
        },
        "RequestId": "326f90c7-6e81-4596-9e11-ec8897cd6aa7"
    }
}
```

