**Example 1: 查询北极星类型的 Trait 列表**

查询北极星类型的 Trait 列表

Input: 

```
tccli camp DescribeTraits --cli-unfold-argument  \
    --ApplicationID app-sb5z5mmj \
    --ProjectID prj-d2bd4gfn \
    --InstanceID ins-xxxx \
    --Filters.0.Name Type \
    --Filters.0.Values deploy polaris \
    --Filters.1.Name ComponentName \
    --Filters.1.Values app \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TraitOnComponents": [
            {
                "ComponentName": "abc",
                "Trait": [
                    {}
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

