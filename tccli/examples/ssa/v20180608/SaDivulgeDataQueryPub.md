**Example 1: 自定义泄露监测列表**



Input: 

```
tccli ssa SaDivulgeDataQueryPub --cli-unfold-argument  \
    --Status 0 \
    --DivulgeSoure 0 \
    --RuleId 0 \
    --RuleName  \
    --EventName  \
    --Limit 5 \
    --Asset  \
    --StartTime 2022-04-05 00:00:00 \
    --Offset 0 \
    --QueryKey  \
    --Level 1,2,3,4 \
    --EndTime 2022-04-12 23:59:59
```

Output: 
```
{
    "Response": {
        "Data": {
            "Count": 641,
            "List": [
                {
                    "Id": "50561",
                    "Uin": "1445149556",
                    "AppId": "1251001047",
                    "EventName": "subash2001/kernel_realme_RMX1821",
                    "DivulgeSoure": "1",
                    "Asset": "",
                    "RuleName": "test",
                    "RuleId": "2946",
                    "RuleWord": "gdb filename test",
                    "ScanUrl": "https://github.com/subash2001/kernel_realme_RMX1821/blob/8d03dd3a8fc7b828f8141415b955ede6623959f8/lib/Kconfig.debug",
                    "ScanCount": "1",
                    "Level": "4",
                    "Status": "1",
                    "EventTime": "2022-04-12 11:22:20",
                    "InsertTime": "2022-04-12 11:22:20",
                    "UpdateTime": "2022-04-12 11:22:20"
                },
                {
                    "Id": "50560",
                    "Uin": "1445149556",
                    "AppId": "1251001047",
                    "EventName": "FrontendGod0123/angular-mst-store",
                    "DivulgeSoure": "1",
                    "Asset": "",
                    "RuleName": "test",
                    "RuleId": "2946",
                    "RuleWord": "gdb filename test",
                    "ScanUrl": "https://github.com/FrontendGod0123/angular-mst-store/blob/1aaafce2e72a0e330fd5670fd24cb0a83508fc78/yarn.lock",
                    "ScanCount": "1",
                    "Level": "4",
                    "Status": "1",
                    "EventTime": "2022-04-12 11:22:20",
                    "InsertTime": "2022-04-12 11:22:20",
                    "UpdateTime": "2022-04-12 11:22:20"
                },
                {
                    "Id": "48397",
                    "Uin": "1445149556",
                    "AppId": "1251001047",
                    "EventName": "ldq1128/ldqtest",
                    "DivulgeSoure": "1",
                    "Asset": "",
                    "RuleName": "快乐种子",
                    "RuleId": "2229",
                    "RuleWord": "广东快乐种子科技有限公司",
                    "ScanUrl": "https://github.com/ldq1128/ldqtest/blob/2f7a79346aa3265093e502892442c31d35db73bd/Python_jobs_cleaned.csv",
                    "ScanCount": "49",
                    "Level": "4",
                    "Status": "1",
                    "EventTime": "2022-04-12 11:18:34",
                    "InsertTime": "2022-03-18 21:32:32",
                    "UpdateTime": "2022-04-12 11:18:34"
                },
                {
                    "Id": "48325",
                    "Uin": "1445149556",
                    "AppId": "1251001047",
                    "EventName": "ammadkh/devices",
                    "DivulgeSoure": "1",
                    "Asset": "",
                    "RuleName": "dsad",
                    "RuleId": "3675",
                    "RuleWord": "dsadsadsadsad",
                    "ScanUrl": "https://github.com/ammadkh/devices/blob/0059d0ab48fd29f960b9b1642db49c919ec06445/data/dummy-data.js",
                    "ScanCount": "54",
                    "Level": "4",
                    "Status": "1",
                    "EventTime": "2022-04-12 09:02:38",
                    "InsertTime": "2022-03-18 11:57:29",
                    "UpdateTime": "2022-04-12 09:02:38"
                },
                {
                    "Id": "48161",
                    "Uin": "1445149556",
                    "AppId": "1251001047",
                    "EventName": "immanuelMM/React-theme-1",
                    "DivulgeSoure": "1",
                    "Asset": "",
                    "RuleName": "dsad",
                    "RuleId": "3675",
                    "RuleWord": "dsadsadsadsad",
                    "ScanUrl": "https://github.com/immanuelMM/React-theme-1/blob/9ebc124f046a4d77632bc453b4bf8641f785ce9e/src/components/Services/index.js",
                    "ScanCount": "60",
                    "Level": "4",
                    "Status": "1",
                    "EventTime": "2022-04-12 09:02:38",
                    "InsertTime": "2022-03-07 16:01:30",
                    "UpdateTime": "2022-04-12 09:02:38"
                }
            ]
        },
        "RequestId": "978a07dd-f787-44cf-ad3b-2f508c55358e"
    }
}
```

