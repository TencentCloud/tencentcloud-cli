**Example 1: Getting vulnerability details**

This example shows you how to get vulnerability details.

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
        "VulName": "Vulnerability name",
        "VulLevel": "HIGH",
        "VulType": "WEB",
        "Description": "Vulnerability description",
        "RepairPlan": "Repair plan",
        "CveId": "CVE-001",
        "Reference": "http://www.qcloud.com"
    }
}
```

