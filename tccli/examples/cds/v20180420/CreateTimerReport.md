**Example 1: 新建定时报表**

新建定时报表

Input: 

```
tccli cds CreateTimerReport --cli-unfold-argument  \
    --TplName tpl-8ad5a3f5 \
    --CntTime 1730455722 \
    --CntCycle 0 \
    --Receivers admin \
    --CntDay 1 \
    --CntDate 2020-12-12 \
    --Remark 测试报表数据 \
    --TemplateId 0 \
    --ReportType 0 \
    --AssetsId 1 \
    --Notification 0 \
    --MissionStart 0
```

Output: 
```
{
    "Response": {
        "RequestId": "8ad5a3f5-fd37-4d77-8448-ab680d513500"
    }
}
```

