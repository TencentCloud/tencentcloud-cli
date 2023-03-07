**Example 1: 全部下载列表**



Input: 

```
tccli cwp DescribeBaselineDownloadList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "TaskId": 1,
                "TaskName": "123",
                "Status": 0,
                "StartTime": "0001-01-01 00:00:00",
                "EndTime": "0001-01-01 00:00:00",
                "DownloadUrl": "http://www.a.b.c"
            },
            {
                "TaskId": 1659337212,
                "TaskName": "baseline_weak_password_2022-08-01 15:00:12",
                "Status": 1,
                "StartTime": "2022-08-01 15:00:12",
                "EndTime": "2022-08-01 15:00:13",
                "DownloadUrl": "https://yunjing-dev-1256299843.cos.ap-guangzhou.myqcloud.com/baseline-weakpassword-20220801-9d17c467-07d5-41e8-b17a-08023b747cdb.csv?q-sign-algorithm=sha1&q-ak=AKIDhKl043NTODrNqE5dghYgnmdIqEPSgDug&q-sign-time=1659337213%3B1659423613&q-key-time=1659337213%3B1659423613&q-header-list=host&q-url-param-list=&q-signature=0b4faed272a2849ab0b1c88a578a5c3302d99321"
            },
            {
                "TaskId": 1659338577,
                "TaskName": "baseline_item_result_2022-08-01 15:22:57",
                "Status": 1,
                "StartTime": "2022-08-01 15:22:57",
                "EndTime": "2022-08-01 15:22:58",
                "DownloadUrl": "https://yunjing-dev-1256299843.cos.ap-guangzhou.myqcloud.com/baseline-item-result20220801-b9a74c51-6d64-476c-94bb-ef4321c23d19.csv?q-sign-algorithm=sha1&q-ak=AKIDhKl043NTODrNqE5dghYgnmdIqEPSgDug&q-sign-time=1659338578%3B1659424978&q-key-time=1659338578%3B1659424978&q-header-list=host&q-url-param-list=&q-signature=5e8a8e35fa56b8ae40b2b75325523b6a272d5a0c"
            },
            {
                "TaskId": 1659340686,
                "TaskName": "baseline_host_view_result_2022-08-01 15:58:06",
                "Status": 1,
                "StartTime": "2022-08-01 15:58:06",
                "EndTime": "2022-08-01 15:58:06",
                "DownloadUrl": "https://yunjing-dev-1256299843.cos.ap-guangzhou.myqcloud.com/baseline-host-view-20220801-334e8211-eece-408c-b7c2-6262799d16bf.csv?q-sign-algorithm=sha1&q-ak=AKIDhKl043NTODrNqE5dghYgnmdIqEPSgDug&q-sign-time=1659340686%3B1659427086&q-key-time=1659340686%3B1659427086&q-header-list=host&q-url-param-list=&q-signature=deb402bb4d3b51a679cc2e88e0571f7d70ea3508"
            },
            {
                "TaskId": 1659341050,
                "TaskName": "baseline_rule_view_result_2022-08-01 16:04:10",
                "Status": 1,
                "StartTime": "2022-08-01 16:04:10",
                "EndTime": "2022-08-01 16:04:10",
                "DownloadUrl": "https://yunjing-dev-1256299843.cos.ap-guangzhou.myqcloud.com/baseline-rule-view-result-20220801-e3e02620-290f-4e09-93a6-93010c39d9d2.csv?q-sign-algorithm=sha1&q-ak=AKIDhKl043NTODrNqE5dghYgnmdIqEPSgDug&q-sign-time=1659341050%3B1659427450&q-key-time=1659341050%3B1659427450&q-header-list=host&q-url-param-list=&q-signature=7946fdb78f6d5197234d3aee67affe6159245bd1"
            },
            {
                "TaskId": 1659341335,
                "TaskName": "baseline_item_view_result_2022-08-01 16:08:55",
                "Status": 1,
                "StartTime": "2022-08-01 16:08:55",
                "EndTime": "2022-08-01 16:08:56",
                "DownloadUrl": "https://yunjing-dev-1256299843.cos.ap-guangzhou.myqcloud.com/baseline-item-view-20220801-a92c6549-5371-4872-b1fc-c1b19cce6e20.csv?q-sign-algorithm=sha1&q-ak=AKIDhKl043NTODrNqE5dghYgnmdIqEPSgDug&q-sign-time=1659341336%3B1659427736&q-key-time=1659341336%3B1659427736&q-header-list=host&q-url-param-list=&q-signature=e59b7a006fd6a9ff2354866eb9b8723b15bc95f1"
            },
            {
                "TaskId": 1659341438,
                "TaskName": "baseline_item_result_2022-08-01 16:10:38",
                "Status": 1,
                "StartTime": "2022-08-01 16:10:38",
                "EndTime": "2022-08-01 16:10:38",
                "DownloadUrl": "https://yunjing-dev-1256299843.cos.ap-guangzhou.myqcloud.com/baseline-item-result-20220801-7281f049-ac13-4572-ae30-b37091be37e1.csv?q-sign-algorithm=sha1&q-ak=AKIDhKl043NTODrNqE5dghYgnmdIqEPSgDug&q-sign-time=1659341438%3B1659427838&q-key-time=1659341438%3B1659427838&q-header-list=host&q-url-param-list=&q-signature=e194a8b23fc811b93706547cacf533d58defe639"
            },
            {
                "TaskId": 1659344330,
                "TaskName": "baseline_rule_view_result_2022-08-01 16:58:50",
                "Status": 1,
                "StartTime": "2022-08-01 16:58:50",
                "EndTime": "2022-08-01 16:58:50",
                "DownloadUrl": "https://yunjing-dev-1256299843.cos.ap-guangzhou.myqcloud.com/baseline-rule-view-result-20220801-9decfcc3-4c03-45c5-8e1e-e2387d81fc9a.csv?q-sign-algorithm=sha1&q-ak=AKIDhKl043NTODrNqE5dghYgnmdIqEPSgDug&q-sign-time=1659344330%3B1659430730&q-key-time=1659344330%3B1659430730&q-header-list=host&q-url-param-list=&q-signature=f4de013652394a87c8f2805304564da81475aa13"
            },
            {
                "TaskId": 1659344370,
                "TaskName": "baseline_rule_view_result_2022-08-01 16:59:30",
                "Status": 1,
                "StartTime": "2022-08-01 16:59:30",
                "EndTime": "2022-08-01 16:59:30",
                "DownloadUrl": "https://yunjing-dev-1256299843.cos.ap-guangzhou.myqcloud.com/baseline-rule-view-result-20220801-e12ac1c4-bf1f-443d-bef5-42b8eb0adf6b.csv?q-sign-algorithm=sha1&q-ak=AKIDhKl043NTODrNqE5dghYgnmdIqEPSgDug&q-sign-time=1659344370%3B1659430770&q-key-time=1659344370%3B1659430770&q-header-list=host&q-url-param-list=&q-signature=2a445f16f3334b835345c8cad77c91443de480dc"
            },
            {
                "TaskId": 1659344382,
                "TaskName": "baseline_rule_view_result_2022-08-01 16:59:42",
                "Status": 1,
                "StartTime": "2022-08-01 16:59:42",
                "EndTime": "2022-08-01 16:59:42",
                "DownloadUrl": "https://yunjing-dev-1256299843.cos.ap-guangzhou.myqcloud.com/baseline-rule-view-result-20220801-6bb54b9e-d2c3-4d4b-a08c-8e6fa12e82b3.csv?q-sign-algorithm=sha1&q-ak=AKIDhKl043NTODrNqE5dghYgnmdIqEPSgDug&q-sign-time=1659344382%3B1659430782&q-key-time=1659344382%3B1659430782&q-header-list=host&q-url-param-list=&q-signature=f4f3c8fb1401858225304d9a9c6cf28f6e8cc8a4"
            }
        ],
        "RequestId": "b0596030-57ec-42aa-8e0f-738a6a07e2d0",
        "Total": 19
    }
}
```

