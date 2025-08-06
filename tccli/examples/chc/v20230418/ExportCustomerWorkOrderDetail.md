**Example 1: 导出客户工单详情**



Input: 

```
tccli chc ExportCustomerWorkOrderDetail --cli-unfold-argument  \
    --WorkOrderType rackOn \
    --BeginDateTime 2025-04-01 00:00:00 \
    --EndDateTime 2025-04-30 00:00:00
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "http://ap-guangzhou-test-1305532550.cos.ap-guangzhou.myqcloud.com/idc_portal_work_order/251233270/251233270_2025-04-01_00-00-00_2025-04-30_00-00-00.xlsx?q-sign-algorithm=sha1&q-ak=xxx&q-sign-time=1749127181%3B1749127541&q-key-time=1749127181%3B1749127541&q-header-list=host&q-url-param-list=&q-signature=3a30d015e08fb524f75b31217d2436bbce70e6ec",
        "RequestId": "591f555e-23b9-4b9a-aab8-186364534732"
    }
}
```

