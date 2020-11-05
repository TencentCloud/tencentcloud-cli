**Example 1: Gets vulnerability list**

This example shows you how to get the vulnerability list.

Input: 

```
tccli yunjing DescribeVuls --cli-unfold-argument  \
    --VulType WEB\
    --Limit 10\
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
                "VulName": "Vulnerability name",
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

