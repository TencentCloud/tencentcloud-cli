**Example 1: 删除自定义函数**

删除自定义函数

Input: 

```
tccli wedata DeleteCustomFunction --cli-unfold-argument  \
    --ClusterIdentifier DLC_hx756s1y \
    --FunctionId 4ecf0901-66ff-4fee-8ad4-b628605d0ff8 \
    --ProjectId 1470547050521227264 \
    --FunctionType DLC
```

Output: 
```
{
    "Response": {
        "ErrorMessage": null,
        "FunctionId": "4ecf0901-66ff-4fee-8ad4-b628605d0ff8",
        "RequestId": "1ac2b0a7-497a-4c7f-883e-8a25f491bdfd"
    }
}
```

