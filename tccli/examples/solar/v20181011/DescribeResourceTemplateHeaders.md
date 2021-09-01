**Example 1: DescribeResourceTemplateHeaders**



Input: 

```
tccli solar DescribeResourceTemplateHeaders --cli-unfold-argument  \
    --WxAppId wx1e62e94ac374e3fb
```

Output: 
```
{
    "Response": {
        "RequestId": "676cfa85-f039-4f1e-b396-85a1aefff805",
        "TotalCount": 1,
        "TmplList": [
            {
                "CanEdit": true,
                "CreateTime": "2020-01-03 09:45:07",
                "TmplId": "662592265872609280",
                "TmplName": "test",
                "TmplTitle": "任务提醒",
                "TmplDesc": "",
                "TmplRemark": ""
            }
        ]
    }
}
```

