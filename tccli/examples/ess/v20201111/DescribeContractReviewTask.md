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
        "PolicyType": 3,
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
                "RiskLevelId": 0,
                "RiskName": "竞业限制期限缺失",
                "RiskPresentation": [
                    "不符合清单要求"
                ]
            }
        ],
        "ApprovedLists": [
            {
                "CategoryName": "合同主体审查",
                "Excerpts": [
                    {
                        "Content": "2.2注册腾讯云账号，甲方应依法具备必要、适当的权利能力和行为能力，已授予操作人足够的权利完成注册过程。甲方必须提交自身合法、真实、有效的身份信息完成真实身份的核验。甲方未提交真实身份信息的、未能通过真实身份核验的，腾讯云依法不对甲方提供服务。",
                        "Position": null
                    }
                ],
                "RiskBasis": "【通用商业合同审查清单】{合同主体审查}, 系统审查要求。",
                "RiskDescription": "1）若签约人为代理人，建议审查需审查授权范围是否涵盖合同标的（如采购金额、租赁期限等）；2）建议审查授权书是否明确排除限制条款（如不得签署担保类协议）。",
                "RiskId": "yDtzVUUHqHYnSLWte",
                "RiskName": "授权权限匹配性"
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

