**Example 1: 修改、删除实例标签**

使用该接口，可以对实例标签进行添加、修改或者删除

Input: 

```
tccli cdb ModifyInstanceTag --cli-unfold-argument  \
    --InstanceId cdb-uns231ns \
    --ReplaceTags.0.TagKey march1 \
    --ReplaceTags.0.TagValue marchtest1
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

