**Example 1: 跳过迁移校验检查项**

当校验不通过时、用户需要跳过校验失败项时、可通过这个接口完成跳过；也可通过这个接口设置是否迁移外键依赖。

Input: 

```
tccli dts SkipCheckItem --cli-unfold-argument  \
    --JobId dts-1ewjspuw \
    --StepIds OptimizeCheck
```

Output: 
```
{
    "Response": {
        "RequestId": "46b45da1-3e8e-4ef2-8de8-b1bffa027385",
        "Message": "skip item successfully"
    }
}
```

