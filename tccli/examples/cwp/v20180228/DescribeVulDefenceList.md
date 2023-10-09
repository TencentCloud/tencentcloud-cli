**Example 1: 示例**



Input: 

```
tccli cwp DescribeVulDefenceList --cli-unfold-argument  \
    --By PublishTime \
    --Limit 20 \
    --Order desc \
    --Filters.0.Values CVE-2022-22963 \
    --Filters.0.Name Keywords \
    --Filters.0.ExactMatch false \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "VulName": "Spring Cloud Function SpEL表达式注入漏洞 (CVE-2022-22963)",
                "Label": "远程利用,存在EXP",
                "Level": 4,
                "CvssScore": 9.8,
                "CveId": "CVE-2022-22963",
                "PublishTime": "2022-03-25 00:00:00"
            }
        ],
        "RequestId": "5eb93566-d6c9-4a07-baba-dc8788f41f19",
        "TotalCount": 3
    }
}
```

