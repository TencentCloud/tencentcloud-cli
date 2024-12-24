**Example 1: 示例**

获取资源绑定DB状态

Input: 

```
tccli dsgc QueryResourceDbBindStatus --cli-unfold-argument  \
    --DspaId dspa-12cd45g7 \
    --ResourceId cdb-adhyf85f \
    --ResourceRegion ap-guangzhou \
    --MetaType cdb
```

Output: 
```
{
    "Response": {
        "BindDbNums": 1,
        "UnbindDbNums": 1,
        "RequestId": "91c7a73v-e540-4780-8b8e-74e0b65b4f1a"
    }
}
```

