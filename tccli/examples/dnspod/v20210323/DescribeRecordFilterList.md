**Example 1: 获取域名的解析记录筛选列表参数示例**

获取域名的解析记录筛选列表

Input: 

```
tccli dnspod DescribeRecordFilterList --cli-unfold-argument  \
    --Domain dnspod.cn \
    --DomainId 1 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RecordCountInfo": {
            "ListCount": 1,
            "SubdomainCount": 27,
            "TotalCount": 27
        },
        "RecordList": [
            {
                "DefaultNS": false,
                "Line": "默认",
                "LineId": "0",
                "MX": 1,
                "MonitorStatus": "",
                "Name": "@",
                "RecordId": 1,
                "Remark": "示例",
                "Status": "ENABLE",
                "TTL": 3600,
                "Type": "CNAME",
                "UpdatedOn": "2022-03-11 14:47:49",
                "Value": "dnspod.cn.",
                "Weight": null
            }
        ],
        "RequestId": "xxx"
    }
}
```

