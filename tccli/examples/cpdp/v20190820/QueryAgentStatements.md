**Example 1: 直播平台-查询代理商结算单链接**



Input: 

```
tccli cpdp QueryAgentStatements --cli-unfold-argument  \
    --Date 2020-05-01 \
    --Type monthly
```

Output: 
```
{
    "Response": {
        "FileUrl": "https://cpdp.cos.ap-guangzhou.myqcloud.com/excel/agent/21521616039/monthly_2020-5.xlsx",
        "RequestId": "784ed425-b2a0-4779-8672-ccd6ea335657"
    }
}
```

