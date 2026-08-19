**Example 1: 云资源配置检测检查规范分类统计**



Input: 

```
tccli csip DescribeComplianceStatistics --cli-unfold-argument  \
    --MemberId mem-00dass
```

Output: 
```
{
    "Response": {
        "Standards": [
            {
                "Count": 114,
                "ID": 4,
                "Name": "网络安全等级保护基本要求（三级）"
            }
        ],
        "TotalCount": 176,
        "RequestId": "466714fe-441d-4a51-9de3-26d7299b9c36"
    }
}
```

