**Example 1: 验证个人版命名空间是否存在**



Input: 

```
tccli tcr ValidateNamespaceExistPersonal --cli-unfold-argument  \
    --Namespace mynamespace
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Data": {
            "IsExist": false,
            "IsPreserved": false
        }
    }
}
```

