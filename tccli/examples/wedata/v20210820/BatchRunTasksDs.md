**Example 1: 成功**

成功

Input: 

```
tccli wedata BatchRunTasksDs --cli-unfold-argument  \
    --ProjectId abc \
    --TaskIds abc \
    --EnableMakeUp 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true,
            "ErrorId": "abc",
            "ErrorDesc": "abc"
        },
        "RequestId": "abc"
    }
}
```

