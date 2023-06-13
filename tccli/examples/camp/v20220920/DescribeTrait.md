**Example 1: 查询 Trait 信息**

查询 Trait 信息

Input: 

```
tccli camp DescribeTrait --cli-unfold-argument  \
    --ApplicationID app-sb5z5mmj \
    --ProjectID prj-d2bd4gfn \
    --InstanceID ins-xxxx \
    --ComponentName app \
    --TraitName app-v1
```

Output: 
```
{
    "Response": {
        "Trait": {},
        "RequestId": "bitliu-rid-xxxxx"
    }
}
```

