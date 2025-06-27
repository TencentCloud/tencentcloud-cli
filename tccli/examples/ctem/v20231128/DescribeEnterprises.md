**Example 1: 查看子公司数据**

查看子公司数据

Input: 

```
tccli ctem DescribeEnterprises --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Abbreviation": "",
                "CreditCode": "",
                "DisplayToolCommon": {
                    "CreateAt": "2024-05-31 11:49:51",
                    "CustomerId": 100081,
                    "CustomerName": "5555",
                    "Detail": "",
                    "EnterpriseName": "",
                    "EnterpriseUid": "ca9476ab116f2ee8ec03684e011df198",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "ca9476ab116f2ee8ec03684e011df198",
                    "UpdateAt": "2024-05-31 11:49:51"
                },
                "EnterpriseUid": "ca9476ab116f2ee8ec03684e011df198",
                "Id": 14593,
                "Industry": "",
                "LegalPerson": "",
                "Name": "aaabb",
                "ParentEnterpriseUid": "",
                "RegisteredCapital": "",
                "ShareholdingRatio": "",
                "Status": "",
                "Type": ""
            },
            {
                "Abbreviation": "",
                "CreditCode": "",
                "DisplayToolCommon": {
                    "CreateAt": "2024-05-31 11:46:12",
                    "CustomerId": 100081,
                    "CustomerName": "5555",
                    "Detail": "",
                    "EnterpriseName": "",
                    "EnterpriseUid": "80b79ef76c27c7bf675591618e07454b",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "80b79ef76c27c7bf675591618e07454b",
                    "UpdateAt": "2024-05-31 11:46:12"
                },
                "EnterpriseUid": "80b79ef76c27c7bf675591618e07454b",
                "Id": 14592,
                "Industry": "",
                "LegalPerson": "",
                "Name": "asss",
                "ParentEnterpriseUid": "",
                "RegisteredCapital": "",
                "ShareholdingRatio": "",
                "Status": "",
                "Type": ""
            }
        ],
        "RequestId": "5c508816-3155-4906-93ce-2e1286697ba6",
        "Total": 2
    }
}
```

