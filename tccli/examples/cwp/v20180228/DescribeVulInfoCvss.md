**Example 1: 漏洞详情，带CVSS版本**

漏洞详情，带CVSS版本

Input: 

```
tccli cwp DescribeVulInfoCvss --cli-unfold-argument  \
    --VulId 100441
```

Output: 
```
{
    "Response": {
        "CveId": "1",
        "CvssScore": 1,
        "Description": "ad",
        "Reference": "fs",
        "VulName": "漏洞1",
        "CveInfo": "",
        "CvssScoreFloat": 9.9,
        "VulType": 1,
        "VulLevel": 2,
        "RequestId": "req-566234234",
        "VulId": 100441,
        "RepairPlan": "13412",
        "CVSS": "AV:L/AC:L/Au:N/C:N/I:P/A:N",
        "PublicDate": "2020-12-30:00:00:00"
    }
}
```

