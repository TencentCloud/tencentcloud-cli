**Example 1: 异步导出 QA**

异步导出 QA

Input: 

```
tccli adp ExportQA --cli-unfold-argument  \
    --FilterList.0.Name Status \
    --FilterList.0.ValueList 3 \
    --KbId 2068959268369066176
```

Output: 
```
{
    "Response": {
        "ExportTaskId": "223780",
        "RequestId": "159e3177-7072-477f-9a18-5486b5074aca"
    }
}
```

