**Example 1: 查询集群参数**



Input: 

```
tccli cynosdb DescribeClusterParams --cli-unfold-argument  \
    --ClusterId cynosdbpg-1xcycbu8
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "MatchValue": "",
                "CurrentValue": "4096",
                "Min": "1024",
                "Default": "4096",
                "Description": "xx",
                "Max": "65536",
                "ParamType": "integer",
                "EnumValue": null,
                "ParamName": "work_mem",
                "MatchType": "",
                "NeedReboot": 0
            },
            {
                "MatchValue": "",
                "CurrentValue": "base64",
                "Min": "",
                "Default": "base64",
                "Description": "xx",
                "Max": "",
                "ParamType": "enum",
                "EnumValue": [
                    "base64",
                    "hex"
                ],
                "ParamName": "xmlbinary",
                "MatchType": "",
                "NeedReboot": 0
            }
        ],
        "RequestId": "117812",
        "TotalCount": 2
    }
}
```

