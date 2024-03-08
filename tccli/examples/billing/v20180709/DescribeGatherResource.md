**Example 1: 查询分账账单资源归集汇总**

查询分账账单资源归集汇总

Input: 

```
tccli billing DescribeGatherResource --cli-unfold-argument  \
    --Month 2024-02 \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "GatherResourceSummary": [
            {
                "ActionType": "prepay_renew",
                "ActionTypeName": "包年包月续费",
                "AllocationType": 1,
                "BelongRule": null,
                "BelongTreeNodeUniqKey": {
                    "TreeNodeUniqKey": "909619400-6391dae9802da",
                    "TreeNodeUniqKeyName": "客户应用组"
                },
                "BusinessCode": "p_mongodb",
                "BusinessCodeName": "云数据库TencentDB for MongoDB",
                "CashPayAmount": "176.43419703",
                "IncentivePayAmount": "0.00000000",
                "InstanceType": "-",
                "InstanceTypeName": "-",
                "ItemCode": "sv_mongodb_mem_replica",
                "ItemCodeName": "文档数据库MongoDB-副本集-内存",
                "OperateUin": "909619400",
                "OtherRules": [],
                "OtherTreeNodeUniqKeys": [],
                "OwnerUin": "909619400",
                "PayMode": "prePay",
                "PayModeName": "包年包月",
                "PayerUin": "909619400",
                "ProductCode": "sp_mongodb_replica",
                "ProductCodeName": "云数据库MongoDB-副本集",
                "ProjectId": 0,
                "ProjectName": "默认项目",
                "RealTotalCost": "176.43419703",
                "RegionId": 1,
                "RegionName": "华南地区（广州）",
                "ResourceId": "cmgo-p46bysvb",
                "ResourceName": null,
                "RuleId": null,
                "RuleName": null,
                "SplitItemId": "",
                "SplitItemName": "",
                "Tag": null,
                "TransferPayAmount": "0.00000000",
                "TreeNodeUniqKey": "909619400-6391dae9802da",
                "TreeNodeUniqKeyName": "客户应用组",
                "VoucherPayAmount": "0.00000000"
            }
        ],
        "LastUpdateTime": "2024-03-02 13:17:07",
        "RecordNum": 3792,
        "RequestId": "b8bedd7a-da43-4cce-ab6e-2fa66ffe1455"
    }
}
```

