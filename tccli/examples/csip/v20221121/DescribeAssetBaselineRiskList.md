**Example 1: 获取主机资产风险列表**

获取主机资产风险列表

Input: 

```
tccli csip DescribeAssetBaselineRiskList --cli-unfold-argument  \
    --AssetUniqueID 87cd7655-**2**4******a1-6267cb76707d \
    --AssetType HOST \
    --AssetAppID 260083796 \
    --MemberId mem-***c**t*6*57*5*5**66e429 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Item": {
                    "AffectedVersionList": [],
                    "Category": {
                        "CheckAssetType": "HOST",
                        "Description": "来自互联网安全中心（CIS）的 CIS Benchmarks 是一套全球公认的共识驱动型最佳实践",
                        "ID": 209,
                        "Name": "国际标准-TencentOS 4安全基线检查"
                    },
                    "CheckObject": [
                        "HOST"
                    ],
                    "CustomItemID": 0,
                    "DefaultValueList": [],
                    "Description": ".netrc文件包含用于通过FTP登录远程主机进行文件传输的认证数据。",
                    "FixSuggestion": "以下脚本将从交互式用户的主目录中移除.netrc文件\n#!/bin/bash\n\nawk -F: '($1!~/(halt|sync|shutdown|nfsnobody)/ && $7!~/^(\\/usr)?\\/sbin\\/nologin(\\/)?$/ && $7!~/(\\/usr)?\\/bin\\/false(\\/)?$/) { print $6 }' /etc/passwd | while read -r dir; do\n\tif [ -d \"$dir\" ]; then\n\t\tfile=\"$dir/.netrc\"\n\t\t[ ! -h \"$file\" ] && [ -f \"$file\" ] && rm -f \"$file\"\n\tfi\ndone",
                    "ID": 5593,
                    "IsCustomConf": false,
                    "Name": "确保所有用户均无.netrc文件",
                    "ReferenceLink": "",
                    "RiskLevel": "LOW",
                    "RuleID": 14584,
                    "SupportCustomValue": false,
                    "SupportFix": false,
                    "SystemCategory": {
                        "CheckAssetType": "HOST",
                        "Description": "来自互联网安全中心（CIS）的 CIS Benchmarks 是一套全球公认的共识驱动型最佳实践",
                        "ID": 2,
                        "Name": "国际通用安全最佳实践基线（CIS）"
                    },
                    "WebEditParam": ""
                },
                "LatestCheckTime": "2026-09-21T19:25:40Z",
                "PolicyInfo": {
                    "ID": 1008,
                    "IsSystem": false,
                    "PolicyName": "vcvbcvb"
                },
                "ResultStatus": "PASS",
                "RiskID": "03d747385c23a17c834615ee0c6f1ea8"
            }
        ],
        "TotalCount": 10,
        "RequestId": "0bd276e2-31f8-4d34-a327-31ca8a8a2ac7"
    }
}
```

