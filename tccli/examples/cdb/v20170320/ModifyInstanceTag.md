**Example 1: Modifying or deleting an instance tag**

This example shows you how to add, modify, or delete an instance tag.

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

