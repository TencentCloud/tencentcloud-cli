**Example 1: 修改分类**

修改分类

Input: 

```
tccli adp ModifyCategory --cli-unfold-argument  \
    --CategoryId 2097580091993756672 \
    --CategoryType 1 \
    --Fields.Name 2423432443242 \
    --KbId 2092085032339506432 \
    --UpdateMask.Paths Name
```

Output: 
```
{
    "Response": {
        "RequestId": "c034503c-b9cb-461c-8b1c-c0bf5d134591"
    }
}
```

