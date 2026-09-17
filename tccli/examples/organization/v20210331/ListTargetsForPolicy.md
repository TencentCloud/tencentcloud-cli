**Example 1: 查询某个指定策略关联的目标列表**

查询某个指定策略关联的目标列表

Input: 

```
tccli organization ListTargetsForPolicy --cli-unfold-argument  \
    --PolicyId 2149848746 \
    --Rp 20 \
    --Page 1 \
    --PolicyType SERVICE_CONTROL_POLICY
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AddTime": "2026-08-18 21:50:42",
                "Name": "基础架构组",
                "NodePath": [
                    "Root",
                    "研发中心",
                    "基础架构组"
                ],
                "NodePathIds": [
                    224674,
                    225415,
                    225418
                ],
                "RelatedType": 1,
                "Uin": 225418
            },
            {
                "AddTime": "2026-08-18 21:50:58",
                "Name": "元数据组",
                "NodePath": [
                    "Root",
                    "研发中心",
                    "基础架构组",
                    "存储小组",
                    "分布式存储",
                    "元数据组"
                ],
                "NodePathIds": [
                    224674,
                    225415,
                    225418,
                    225421,
                    225422,
                    225423
                ],
                "RelatedType": 1,
                "Uin": 225423
            },
            {
                "AddTime": "2026-08-18 16:08:18",
                "Name": "testCIC2",
                "NodePath": [
                    "Root",
                    "研发中心",
                    "基础架构组",
                    "存储小组",
                    "分布式存储",
                    "元数据组",
                    "testCIC2"
                ],
                "NodePathIds": [
                    224674,
                    225415,
                    225418,
                    225421,
                    225422,
                    225423,
                    700003086465
                ],
                "RelatedType": 2,
                "Uin": 700003086465
            }
        ],
        "RequestId": "0816fb00-e6c3-4583-9754-4b561dda0f1a",
        "TotalNum": 3
    }
}
```

