**Example 1: 导出java内存马插件列表**

导出

Input: 

```
tccli cwp ExportJavaMemShellPlugins --cli-unfold-argument  \
    --Filters.0.Name Quuid \
    --Filters.0.Values d4cc302e-09e5-436f-b99b-5ab9c9070323
```

Output: 
```
{
    "Response": {
        "RequestId": "d92d723e-4aac-4f4a-bbf9-e5430e29d289",
        "TaskId": "187653"
    }
}
```

