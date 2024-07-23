**Example 1: 根据模板ID查询参数模板**



Input: 

```
tccli mongodb DescribeDBInstanceParamTpl --cli-unfold-argument  \
    --TplIds tpl-eykkk2khs
```

Output: 
```
{
    "Response": {
        "ParamTpls": [
            {
                "ClusterType": "REPLSET",
                "MongoVersion": "MONGO_42_WT",
                "TplDesc": "System predefined, forbid modify and delete.",
                "TplId": "tpl-eykkk2khs",
                "TplName": "default parameter template",
                "TplType": "DEFAULT"
            }
        ],
        "RequestId": "7878d7d7-8c80-4050-93a1-5e1785effd1a",
        "TotalCount": 1
    }
}
```

