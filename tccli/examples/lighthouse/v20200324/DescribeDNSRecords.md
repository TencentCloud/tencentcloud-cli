**Example 1: 查询解析记录**



Input: 

```
tccli lighthouse DescribeDNSRecords --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "b11db5bc-f6fd-4a4c-9035-b289af22d98f",
        "TotalCount": 2,
        "RecordSet": [
            {
                "RecordId": "lhdr-jxj6qkjw",
                "Subdomain": "aa",
                "RecordState": "NORMAL",
                "RecordType": "A",
                "RecordValue": "2.3.4.5",
                "ResourceType": "",
                "ResourceKey": "",
                "ResourceRegion": "",
                "DomainId": "lhdo-3ob8xfuu",
                "DomainName": "lhsday.com",
                "CreatedTime": "2022-09-27T03:29:22Z",
                "UpdatedTime": "2022-09-27T03:29:22Z"
            },
            {
                "RecordId": "lhdr-qpnq8qzk",
                "Subdomain": "www",
                "RecordState": "NORMAL",
                "RecordType": "A",
                "RecordValue": "1.2.3.4",
                "ResourceType": "",
                "ResourceKey": "",
                "ResourceRegion": "",
                "DomainId": "lhdo-3ob8xfuu",
                "DomainName": "lhsday.com",
                "CreatedTime": "2022-09-27T03:29:22Z",
                "UpdatedTime": "2022-09-27T03:29:22Z"
            }
        ]
    }
}
```

