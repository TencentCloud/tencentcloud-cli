**Example 1: 获取Api安全模块的访问日志聚合topN**

示例描述

Input: 

```
tccli waf DescribeApiAggregateTopN --cli-unfold-argument  \
    --TopN 5 \
    --Domain hzh.qcloud.com \
    --StartTs 666123231 \
    --EndTs 666123156 \
    --Dimension attack_type
```

Output: 
```
{
    "Response": {
        "RequestId": "02e6870f-89b6-4e7b-b738-942ef9bfd1e5",
        "Data": [
            {
                "Key": "luffy",
                "Value": 100,
                "Label": "custom"
            }
        ]
    }
}
```

