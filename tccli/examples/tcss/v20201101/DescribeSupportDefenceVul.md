**Example 1: 查询支持防御的漏洞列表**



Input: 

```
tccli tcss DescribeSupportDefenceVul --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "List": [
            {
                "CVEID": "xx",
                "Name": "xx",
                "Level": "xx",
                "CVSSV3Score": 0.0,
                "Tags": [
                    "xx"
                ],
                "SubmitTime": "xx",
                "PocID": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

