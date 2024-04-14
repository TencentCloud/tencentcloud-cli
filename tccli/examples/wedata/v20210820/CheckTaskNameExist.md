**Example 1: 离线任务重名校验**



Input: 

```
tccli wedata CheckTaskNameExist --cli-unfold-argument  \
    --ProjectId 11022568003970304 \
    --TaskName testTaskName \
    --TypeId 27
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

