**Example 1: 离线任务重名校验**



Input: 

```
tccli wedata CheckTaskNameExist --cli-unfold-argument  \
    --ProjectId abc \
    --TaskName abc \
    --TypeId 27
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

