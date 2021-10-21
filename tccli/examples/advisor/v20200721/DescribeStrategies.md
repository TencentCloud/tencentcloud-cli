**Example 1: 查询评估项信息**



Input: 

```
tccli advisor DescribeStrategies --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "111",
        "Strategies": [
            {
                "StrategyId": 131,
                "Name": "云数据库（Redis）跨可用区部署",
                "Desc": "检查 Redis 实例是否跨可用区部署，如果实例未跨可用区部署，当实例出现可用区级别的灾难故障时，可能造成实例无法访问风险",
                "Product": "redis",
                "ProductDesc": "云数据库（Redis）",
                "Repair": "如果业务有较高容灾需求，建议采用跨可用区部署方案，提升业务可靠性，[跨可用区分布操作指引](https://cloud.tencent.com/document/product/239/51113)",
                "GroupId": 2,
                "GroupName": "可靠",
                "Conditions": [
                    {
                        "ConditionId": 178,
                        "Level": 2,
                        "LevelDesc": "中风险",
                        "Desc": "Redis 实例未跨可用区部署"
                    }
                ]
            },
            {
                "StrategyId": 235,
                "Name": "云数据库（Redis）使用基础网络",
                "Desc": "检查 Redis 是否使用基础网络",
                "Product": "redis",
                "ProductDesc": "云数据库（Redis）",
                "Repair": "建议更换为私有网络，私有网络是一块逻辑隔离的网络空间，基础网络是腾讯云上所有用户的公共网络资源池",
                "GroupId": 2,
                "GroupName": "可靠",
                "Conditions": [
                    {
                        "ConditionId": 307,
                        "Level": 2,
                        "LevelDesc": "中风险",
                        "Desc": "实例使用基础网络"
                    }
                ]
            }
        ]
    }
}
```

