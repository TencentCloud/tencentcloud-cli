**Example 1: 查询函数下的全部别名**



Input: 

```
tccli scf ListAliases --cli-unfold-argument  \
    --Namespace <Namespace> \
    --FunctionName <FunctionName>
```

Output: 
```
{
    "Response": {
        "RequestId": "d1b93f9c-ac3a-412a-a4f3-6f0697099f72",
        "EipUseNum": 4,
        "EipUserQuota": 5,
        "EipTotalUseNum": 80,
        "EipTotalQuota": 200
    }
}
```

