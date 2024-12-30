**Example 1: 获取记录信息**

 获取记录信息

Input: 

```
tccli dnspod DescribeRecord --cli-unfold-argument  \
    --Domain dnspod.site \
    --DomainId 62 \
    --RecordId 162
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "RecordInfo": {
            "Id": 158,
            "SubDomain": "www",
            "RecordType": "A",
            "RecordLine": "百度",
            "RecordLineId": "90=0",
            "Value": "129.23.32.32",
            "Weight": null,
            "MX": 0,
            "TTL": 10,
            "Enabled": 1,
            "MonitorStatus": "Ok",
            "Remark": "备注",
            "UpdatedOn": "2021-03-31 11:38:02",
            "DomainId": 62
        }
    }
}
```

