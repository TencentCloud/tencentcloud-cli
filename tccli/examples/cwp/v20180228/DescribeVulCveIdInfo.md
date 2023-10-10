**Example 1: CveId查询漏洞详情**

CveId查询漏洞详情

Input: 

```
tccli cwp DescribeVulCveIdInfo --cli-unfold-argument  \
    --CveIds CVE-2021-31805
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "FixSwitch": 1,
                "VulId": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

