**Example 1: 查看漏洞分组数据**

查看漏洞分组数据

Input: 

```
tccli ctem DescribeVulGroups --cli-unfold-argument  \
    --CustomerId 100081
```

Output: 
```
{
    "Response": {
        "DownloadLink": "",
        "List": [
            {
                "AffectedAssets": 1,
                "AffectedEnterprises": [],
                "Component": "",
                "Level": 0,
                "Name": "test",
                "Type": ""
            }
        ],
        "RequestId": "560758cc-cfb0-4642-b6d1-df1218a34115",
        "Total": 1
    }
}
```

