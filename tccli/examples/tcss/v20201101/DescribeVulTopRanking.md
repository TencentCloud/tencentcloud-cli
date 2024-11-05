**Example 1: 查询漏洞Top排名列表**



Input: 

```
tccli tcss DescribeVulTopRanking --cli-unfold-argument  \
    --CategoryType SYSTEM
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AffectedContainerCount": 0,
                "AffectedImageCount": 1,
                "ID": 1027671,
                "Level": "HIGH",
                "PocID": "pcmgr-166817",
                "VulName": "Telnetd encrypt_keyid: Remote Root function pointer overwrite"
            }
        ],
        "RequestId": "ce6b8df8-5cc6-4ab5-8401-1394483c0fec"
    }
}
```

