**Example 1: 删除词库范例**



Input: 

```
tccli cms DeleteKeywordsLib --cli-unfold-argument  \
    --UserAppID xx \
    --UserUin xx \
    --ID xx \
    --UserSubUin xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

**Example 2: 删除词库示例**



Input: 

```
tccli cms DeleteKeywordsLib --cli-unfold-argument  \
    --UserUin 123 \
    --UserSubUin 123 \
    --UserAppID 123 \
    --ID 4c49c04f-6617-4705-b3ff-bedce642bfcb
```

Output: 
```
{
    "Response": {
        "RequestId": "adddea6d-8abb-45a7-bcfe-8c7f0bb999d8"
    }
}
```

