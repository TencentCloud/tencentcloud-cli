**Example 1: 示例**

获取DSPA实例的版本体验信息

Input: 

```
tccli dsgc GetTrialVersion --cli-unfold-argument  \
    --DspaId abc
```

Output: 
```
{
    "Response": {
        "TrialVersion": "abc",
        "TrialEndAt": 1,
        "RequestId": "abc"
    }
}
```

