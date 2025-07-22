**Example 1: 查询 Agent 列表**



Input: 

```
tccli monitor DescribeScrapeAgents --cli-unfold-argument  \
    --InstanceId prom-abcd
```

Output: 
```
{
    "Response": {
        "Agents": [
            {
                "Source": "cls-abc"
            }
        ],
        "Count": 1,
        "RequestId": "bfa18d10-fe18-4f0e-b7e8-18857f951655"
    }
}
```

