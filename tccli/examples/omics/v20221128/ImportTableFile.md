**Example 1: 导入表格文件**

导入表格文件。

Input: 

```
tccli omics ImportTableFile --cli-unfold-argument  \
    --ProjectId prj-aggressive-lime-porcupine-752427 \
    --Name test_table \
    --Description 测试表格 \
    --CosUri cos://bucket/test.csv \
    --DataType String File
```

Output: 
```
{
    "Response": {
        "TableId": "tab-fancy-saffron-slug-701244",
        "RequestId": "50d781c7-eab9-4339-93ed-c312a2452d9d"
    }
}
```

