**Example 1: 获取漏洞扫描任务详情**



Input: 

```
tccli csip DescribeVulScanTaskDetail --cli-unfold-argument  \
    --Id 127 \
    --Filters.0.Name InstanceId \
    --Filters.0.Values ins-2f***t2k \
    --Limit 2 \
    --Offset 0 \
    --Order DESC \
    --By CreateTime
```

Output: 
```
{
    "Response": {
        "EndTime": "2026-06-10T13:33:00Z",
        "Failed": 24,
        "List": [
            {
                "AppId": 260083796,
                "Description": "",
                "EndTime": "2026-06-10T12:33:13Z",
                "Id": "2346",
                "InstanceId": "ins-2f****2k",
                "InstanceName": "tke_cls-dqum4px0_master_etcd3",
                "OS": "TencentOS Server 3.1 (Final)",
                "PrivateIp": "172.16.0.108",
                "PublicIp": "",
                "StartTime": "2026-06-10T12:32:44Z",
                "Status": "SUCCESS",
                "Vuls": 0
            }
        ],
        "Progress": 100,
        "Risk": 1,
        "Scanned": 51,
        "StartTime": "2026-06-10T12:31:14Z",
        "TaskExcel": "https://*****r*-1**8*4**99.cos.ap-guangzhou.myqcloud.com/vul*s*an**",
        "TaskPdf": "https://*****r*-1**8*4**99.cos.ap-guangzhou.myqcloud.com/vul*s*an**",
        "Total": 1,
        "Vuls": 1,
        "RequestId": "4df6736c-24d7-48e9-8876-dde3a615328b"
    }
}
```

