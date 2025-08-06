**Example 1: 查询合同审查任务详情**



Input: 

```
tccli ess DescribeContractReviewTask --cli-unfold-argument  \
    --Operator.UserId yDwJGxxrmBe \
    --TaskId yDtIFxxxq
```

Output: 
```
{
    "Response": {
        "ChecklistId": "yDtCMxxxxIi",
        "CreatedOn": 1753417470,
        "FinishedOn": 1753417684,
        "PolicyType": 2,
        "RequestId": "s1753417731216986125",
        "ResourceId": "yDtG1UUxxxEsrBwa",
        "Risks": [
            {
                "Content": "第三十二条乙方应当保守甲方的商业秘密，商业秘密系指不为公众所知悉，能为甲方带来经济利益，具有实用性并经甲方采取保密措施的技术秘密和经营信息。包括但不限于下述内容:",
                "RiskAdvice": "建议在第三十二条后增加：「乙方离职后的竞业限制期限不得超过两年，竞业限制补偿金标准为......」",
                "RiskBasis": "【通用商业合同审查清单】{特殊类型合同补充要点}, 系统审查要求。",
                "RiskDescription": "保密条款未明确竞业限制期限，存在超出法定期限的法律风险，可能被认定为无效条款。",
                "RiskId": "yDtIFUU2tnxxxKveWxm",
                "RiskLevel": "NORMAL",
                "RiskName": "竞业限制期限缺失",
                "RiskPresentation": [
                    "不符合清单要求"
                ]
            }
        ],
        "Role": {
            "Description": "",
            "Name": "授权方"
        },
        "Status": 4,
        "TaskId": "yDtIFxxxq"
    }
}
```

