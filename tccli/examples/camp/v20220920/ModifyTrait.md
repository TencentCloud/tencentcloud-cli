**Example 1: 修改 北极星类型 Trait**

修改 北极星类型 Trait

Input: 

```
tccli camp ModifyTrait --cli-unfold-argument  \
    --ApplicationID app-sb5z5mmj \
    --ProjectID prj-d2bd4gfn \
    --InstanceID ins-xxxx \
    --ComponentName app \
    --Trait.Name app-v1 \
    --Trait.Type polaris
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

