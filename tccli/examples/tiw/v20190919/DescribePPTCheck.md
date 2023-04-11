**Example 1: 查询PPT检测任务异常**

查询PPT检测任务，存在异常

Input: 

```
tccli tiw DescribePPTCheck --cli-unfold-argument  \
    --TaskId g0jb42ps49vtebjshilb \
    --SdkAppId 1400000001
```

Output: 
```
{
    "Response": {
        "TaskId": "bj0mt2l23osdj300hl30",
        "IsOK": false,
        "Status": "FINISHED",
        "Progress": 100,
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851",
        "ResultUrl": "https://xxx/xxx/测试_fixed.ppt",
        "Slides": [
            {
                "Page": "幻灯片5",
                "Errs": [
                    {
                        "Name": "Ink 1",
                        "Type": 0,
                        "Detail": "wps墨迹"
                    }
                ]
            }
        ]
    }
}
```

**Example 2: 查询PPT检测任务无异常**

查询PPT检测任务，PPT无异常

Input: 

```
tccli tiw DescribePPTCheck --cli-unfold-argument  \
    --TaskId g0jb42ps49vtebjshilb \
    --SdkAppId 1400000001
```

Output: 
```
{
    "Response": {
        "TaskId": "bj0mt2l23osdj300hl30",
        "IsOK": true,
        "Status": "FINISHED",
        "Progress": 100,
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851",
        "ResultUrl": null,
        "Slides": null
    }
}
```

