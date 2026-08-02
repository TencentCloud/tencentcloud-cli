**Example 1: 变配检查**

变配检查

Input: 

```
tccli es CheckUpdateInstance --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx \
    --NodeType ES.S1.MEDIUM4 \
    --DiskSize 150
```

Output: 
```
{
    "Response": {
        "AllowUpdate": true,
        "RequestId": "dd3f624d-9a72-4057-85cb-f5d32exxxxxx",
        "ErrMsg": "error"
    }
}
```

