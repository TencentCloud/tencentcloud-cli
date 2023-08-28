**Example 1: 更新应用白名单**



Input: 

```
tccli bcrpc ModifySecurityList --cli-unfold-argument  \
    --Name abc \
    --Type 0 \
    --Operate 0 \
    --Value abc
```

Output: 
```
{
    "Response": {
        "RequestId": "ab"
    }
}
```

