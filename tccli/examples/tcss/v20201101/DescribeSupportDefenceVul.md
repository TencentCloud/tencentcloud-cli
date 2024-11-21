**Example 1: 查询支持防御的漏洞列表**



Input: 

```
tccli tcss DescribeSupportDefenceVul --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CVEID": "CVE-2024-23897",
                "CVSSV3Score": 9.8,
                "Level": "CRITICAL",
                "Name": "Jenkins任意文件读取导致远程代码执行漏洞(CVE-2024-23897)",
                "PocID": "pcmgr-469627",
                "Status": 1,
                "SubmitTime": "2024-01-25 02:15:00",
                "Tags": [
                    "NETWORK",
                    "POC"
                ],
                "VulId": 469627
            }
        ],
        "RequestId": "16b04354-f64d-4d6b-821d-125b3f721d5b",
        "TotalCount": 212
    }
}
```

