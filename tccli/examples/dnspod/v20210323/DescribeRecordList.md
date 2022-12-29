**Example 1: 查询域名的解析记录**

 

Input: 

```
tccli dnspod DescribeRecordList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2 \
    --Domain shenjianing.com \
    --DomainId 123 \
    --Subdomain www \
    --Keyword dnspod \
    --RecordType NS \
    --RecordLine 默认 \
    --RecordLineId 0 \
    --SortField type \
    --SortType ASC \
    --GroupId 34
```

Output: 
```
{
    "Response": {
        "RequestId": "561cdfcb-37a6-47de-b3c5-2b038e2c2276",
        "RecordCountInfo": {
            "SubdomainCount": 2,
            "TotalCount": 2,
            "ListCount": 2
        },
        "RecordList": [
            {
                "RecordId": 556507778,
                "Value": "f1g1ns1.dnspod.net.",
                "Status": "ENABLE",
                "UpdatedOn": "2021-03-28 11:27:09",
                "Name": "@",
                "Line": "默认",
                "LineId": "0",
                "Type": "NS",
                "Weight": null,
                "MonitorStatus": "",
                "Remark": "",
                "TTL": 86400,
                "MX": 0
            },
            {
                "RecordId": 556507779,
                "Value": "f1g1ns2.dnspod.net.",
                "Status": "ENABLE",
                "UpdatedOn": "2021-03-28 11:27:09",
                "Name": "@",
                "Line": "默认",
                "LineId": "0",
                "Type": "NS",
                "Weight": null,
                "MonitorStatus": "",
                "Remark": "",
                "TTL": 86400,
                "MX": 0
            }
        ]
    }
}
```

