**Example 1: 获取合规配置**



Input: 

```
tccli sag DescribeCompliance --cli-unfold-argument  \
    --Os Windows
```

Output: 
```
{
    "Response": {
        "Data": {
            "CycleCheck": 1,
            "CycleInterval": 10,
            "FixRemind": 1
        },
        "RequestId": "xx"
    }
}
```

