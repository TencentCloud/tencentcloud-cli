**Example 1: 跨账号克隆数据到指定时间**

dbBrain会对实例进行跨账号克隆，用于不用场景的测试

Input: 

```
tccli cdb CreateCrossAccountCloneTask --cli-unfold-argument  \
    --SrcInstanceId cdb-594gwq4l \
    --DstAppId 121346515 \
    --DstInstanceId cdb-sfesfdvsdf \
    --DryRun False \
    --SpecifiedRollbackTime 2020-08-0116:27:43
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "JobId": "256117ed-efa08b54-61784d44-91781bbd"
    }
}
```

