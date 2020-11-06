**Example 1: 获取漏洞列表**

获取所有漏洞相关信息列表

Input: 

```
tccli cwp DescribeVuls --cli-unfold-argument  \
    --VulType WEB \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "Vuls": [
            {
                "VulId": 4,
                "VulName": "漏洞名称",
                "VulLevel": "HIGHT",
                "VulStatus": "FIXED",
                "LastScanTime": "2018-03-19 17:38:56",
                "ImpactedHostNum": 10
            }
        ],
        "TotalCount": 10
    }
}
```

