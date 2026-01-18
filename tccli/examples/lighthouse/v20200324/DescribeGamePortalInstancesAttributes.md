**Example 1: 查询游戏专区实例属性**



Input: 

```
tccli lighthouse DescribeGamePortalInstancesAttributes --cli-unfold-argument  \
    --InstanceIds lhins-8lj6vg8p
```

Output: 
```
{
    "Response": {
        "GamePortalInstanceAttributesSet": [
            {
                "InstanceId": "lhins-8lj6vg8p",
                "ServerPort": "9999"
            }
        ],
        "RequestId": "08f8b4b7-8bc8-4226-a3e2-56f2024c7abf"
    }
}
```

