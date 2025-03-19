**Example 1: DescribeAsrHotwordsList**



Input: 

```
tccli mps DescribeAsrHotwordsList --cli-unfold-argument  \
    --HotwordsId hwd-aexxxxxxxxxxxxxx1481
```

Output: 
```
{
    "Response": {
        "AsrHotwordsSet": [
            {
                "CreateTime": "2025-03-19T03:29:06Z",
                "FileName": "",
                "HotwordsId": "hwd-aexxxxxxxxxxxxxx1481",
                "Name": "HotwordsNameExample",
                "Status": 0,
                "Type": 0,
                "UpdateTime": "2025-03-19T03:29:06Z",
                "WordCount": 3
            }
        ],
        "Limit": 0,
        "Offset": 0,
        "RequestId": "0beec64c-8390-43dd-8b3a-14df16cc9ca7",
        "TotalCount": 1
    }
}
```

