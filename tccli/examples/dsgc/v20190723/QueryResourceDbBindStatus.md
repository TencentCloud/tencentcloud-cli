**Example 1: 示例**

获取资源绑定DB状态

Input: 

```
tccli dsgc QueryResourceDbBindStatus --cli-unfold-argument  \
    --DspaId abc \
    --ResourceId abc \
    --ResourceRegion abc \
    --MetaType abc
```

Output: 
```
{
    "Response": {
        "BindDbNums": 1,
        "UnbindDbNums": 1,
        "RequestId": "abc"
    }
}
```

