**Example 1: 成功**

成功

Input: 

```
tccli wedata CheckTaskNameExistDs --cli-unfold-argument  \
    --ProjectId abc \
    --TaskName abc \
    --TaskId abc \
    --ProductName abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "IfExist": true,
            "Message": "abc"
        },
        "RequestId": "abc"
    }
}
```

