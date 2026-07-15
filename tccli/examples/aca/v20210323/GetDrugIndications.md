**Example 1: 获取药品适应症示例**

获取药品适应症

Input: 

```
tccli aca GetDrugIndications --cli-unfold-argument  \
    --Header.HospitalId 001 \
    --Header.Token tai.4d563878587a67774d44417a4e544d344e413d3d.1959c3405c614d709babfad5e1b79d54 \
    --Data.Drugs.0.DrugName 诺氟沙星片 \
    --Data.Drugs.0.Specifications 0.1g*36片/盒 \
    --Data.Drugs.0.ApprovalNumber 国药准字H13022772 \
    --Data.Drugs.0.Manufacturer 石药集团欧意药业有限公司
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": {
            "DocInfos": [
                {
                    "DocUrl": "https://dev-aimedical.wecity.qq.com/toolbox/AssistantDetail.html?detailid=04e2bd6dff6422772447fd8c7cd7b5723dd4f7d4&type=drug&token=tai.4d563878587a67774d44417a4e544d344e413d3d.1959c3405c614d709babfad5e1b79d54",
                    "DrugId": "",
                    "DrugName": "诺氟沙星片"
                }
            ],
            "Indications": [
                "感染",
                "淋病",
                "伤寒",
                "其他沙门菌感染",
                "肠道感染",
                "前列腺炎",
                "尿路感染",
                "沙门菌感染"
            ]
        },
        "Message": "success",
        "RequestId": "c6419e0f-7ccb-4fdb-af09-b330d4885f38"
    }
}
```

