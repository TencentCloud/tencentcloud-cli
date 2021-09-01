**Example 1: 获取漏洞详情**

获取漏洞详情

Input: 

```
tccli yunjing DescribeVulInfo --cli-unfold-argument  \
    --VulId 1001
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "VulId": 1001,
        "VulName": "漏洞名称",
        "VulLevel": "HIGH",
        "VulType": "WEB",
        "Description": "漏洞描述信息",
        "RepairPlan": "修复方案",
        "CveId": "CVE-001",
        "Reference": "http://www.qcloud.com"
    }
}
```

