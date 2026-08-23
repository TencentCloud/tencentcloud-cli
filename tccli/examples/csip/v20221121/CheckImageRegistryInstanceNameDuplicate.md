**Example 1: 检查镜像仓库实例名是否重复**



Input: 

```
tccli csip CheckImageRegistryInstanceNameDuplicate --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Name s*******
```

Output: 
```
{
    "Response": {
        "IsDuplicated": false,
        "RequestId": "76bb31a3-e708-4b40-9320-270f36de2e9d"
    }
}
```

