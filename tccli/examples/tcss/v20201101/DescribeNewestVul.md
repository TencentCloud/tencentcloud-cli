**Example 1: 查询最新披露漏洞列表**



Input: 

```
tccli tcss DescribeNewestVul --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CVEID": "pcmgr-515959",
        "PocID": "pcmgr-515959",
        "RequestId": "5da5a2f4-2945-47d1-8b41-84a151fcc007",
        "Status": "SCANNED",
        "SubmitTime": "2024-08-27 09:55:12",
        "VulName": "Nacos Jraft 远程代码执行漏洞"
    }
}
```

