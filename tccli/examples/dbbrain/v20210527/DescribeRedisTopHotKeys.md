**Example 1: 查询热Key分析**



Input: 

```
tccli dbbrain DescribeRedisTopHotKeys --cli-unfold-argument  \
    --Product redis \
    --InstanceId crs-179943dsc \
    --StartTime 2024-09-22T00:00:00+00:00 \
    --EndTime 2024-09-22T01:00:00+00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "75421bae-7fcb-4b32-83df-d66b060b4cbf",
        "TopHotKeys": [
            {
                "Count": 100,
                "Db": "0",
                "InstanceNodeId": "fa765e5e2e432806328a691d591e47097ecd133d",
                "Key": "string|key:000000096",
                "Type": "string"
            }
        ]
    }
}
```

