**Example 1: 导出高危命令事件**

导出高危命令事件

Input: 

```
tccli cwp ExportBashEventsNew --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "DownloadUrl": "http://download.url/test.csv",
        "TaskId": "1133345"
    }
}
```

