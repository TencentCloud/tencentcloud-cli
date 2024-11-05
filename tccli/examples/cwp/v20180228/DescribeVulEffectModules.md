**Example 1: 漏洞影响主机列表**

漏洞影响主机列表

Input: 

```
tccli cwp DescribeVulEffectModules --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --VulId 100435
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "VulEffectModuleInfo": [
            {
                "Name": "openssl-devel",
                "Version": "1:1.0.2k-19.el7",
                "FixCmd": "sudo yum update openssl-devel\n",
                "Path": "/usr/include/openssl",
                "Rule": "openssl-devel version less than 1:1.0.2k-22.el7_9",
                "Uuids": [
                    "05f0bcab-726c-4ea4-8109-bcd03d5598f7"
                ],
                "Quuids": [
                    "05f0bcab-726c-4ea4-8109-bcd03d5598f7"
                ]
            }
        ],
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c"
    }
}
```

