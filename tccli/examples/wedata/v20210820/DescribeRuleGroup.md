**Example 1: 查询规则组详情接口**



Input: 

```
tccli wedata DescribeRuleGroup --cli-unfold-argument  \
    --ProjectId 5678987645 \
    --DatabaseId 5rtfygfty6767tyug \
    --TableId 56tdryfccfyrt556t \
    --DatasourceId 44567 \
    --RuleGroupId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": null,
            "DatabaseId": null,
            "DatabaseName": "v_vzjfzng",
            "DatasourceId": null,
            "DatasourceName": "hive_er-o5bxp",
            "DatasourceType": 2,
            "ExecStrategy": null,
            "InstanceId": "emr-ovzb5bxp",
            "MonitorStatus": true,
            "MonitorType": null,
            "Permission": true,
            "RuleCount": 0,
            "RuleGroupId": null,
            "Subscription": null,
            "TableId": "XuKflA-wQbbohxQbg",
            "TableName": "test",
            "TableOwnerName": "zheyuang",
            "TableOwnerUserId": null,
            "UpdateTime": null
        },
        "RequestId": "7c8ef235-4c4f-4b8b-8-0303d9dc1"
    }
}
```

