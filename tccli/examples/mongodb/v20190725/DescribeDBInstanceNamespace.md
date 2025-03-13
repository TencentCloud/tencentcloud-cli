**Example 1: 查询当前实例的DB列表。**

输入参数 DbName 为空时，查看当前实例全部数据库列表。

Input: 

```
tccli mongodb DescribeDBInstanceNamespace --cli-unfold-argument  \
    --InstanceId cmgo-qny2****
```

Output: 
```
{
    "Response": {
        "Databases": [
            "demo_db7",
            "demo_db8",
            "demo_db9"
        ],
        "RequestId": "18cfe2bf-6934-4f17-a089-8d2e5d6cfc53"
    }
}
```

**Example 2: 查询指定 DB 下的所有集合**

指定 DbName，查询该数据库下的所有集合信息。

Input: 

```
tccli mongodb DescribeDBInstanceNamespace --cli-unfold-argument  \
    --InstanceId cmgo-qny2**** \
    --DbName demo_db0
```

Output: 
```
{
    "Response": {
        "Collections": [
            "col148",
            "col108",
            "col120"
        ],
        "RequestId": "21b503b5-6606-4efb-b250-63071c2fe565"
    }
}
```

