**Example 1: 离线任务重名校验**



Input: 

```
tccli wedata CheckTaskNameExist --cli-unfold-argument  \
    --ProjectId xx \
    --TaskName xx \
    --TypeId 27
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "xx"
    }
}
```

