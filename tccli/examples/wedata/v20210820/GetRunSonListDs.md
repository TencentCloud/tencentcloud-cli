**Example 1: 成功**

成功

Input: 

```
tccli wedata GetRunSonListDs --cli-unfold-argument  \
    --ProjectId abc \
    --WorkflowId abc \
    --TaskId abc
```

Output: 
```
{
    "Response": {
        "Data": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

