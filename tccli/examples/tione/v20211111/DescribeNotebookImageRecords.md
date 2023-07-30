**Example 1: 查看notebook镜像保存记录示例**

查看notebook镜像保存记录示例

Input: 

```
tccli tione DescribeNotebookImageRecords --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 10,
        "NotebookImageRecords": [
            {
                "RecordId": "1",
                "ImageUrl": "ti.com/repo/test:1",
                "Status": "sucess",
                "CreateTime": "2022-01-01 00:00:00",
                "Message": "保存成功"
            }
        ],
        "RequestId": "xx"
    }
}
```

