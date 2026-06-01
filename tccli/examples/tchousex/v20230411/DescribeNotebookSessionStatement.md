**Example 1: 查询代码执行结果**



Input: 

```
tccli tchousex DescribeNotebookSessionStatement --cli-unfold-argument  \
    --SessionId livy-session-8pu64i \
    --StatementId 2
```

Output: 
```
{
    "Response": {
        "RequestId": "c8b7fd14-ea08-43a5-8f8a-4f429a99c99a",
        "ErrorMsg": "",
        "NotebookSessionStatement": {
            "StatementId": "2",
            "Code": "val a = 1\nval b = 2\nval c = a + b\nprintln(\"hello scala\")\nprintln(c)\n",
            "Output": {
                "Status": "ok",
                "ExecutionCount": 2,
                "Data": "{\"text/plain\":\"a: Int = 1\\nb: Int = 2\\nc: Int = 3\\nhello scala\\n3\\n\"}"
            },
            "State": "available",
            "Progress": 1,
            "Started": 1737381354712,
            "Completed": 1737381355518
        }
    }
}
```

