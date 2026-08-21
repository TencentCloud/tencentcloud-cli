**Example 1: 调用示例**



Input: 

```
tccli csip DescribeBaselineSubTaskList --cli-unfold-argument  \
    --TaskID 1389 \
    --MemberId mem-tencent-6*************29
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Appid": 200000000,
                "CheckAssetType": "CLUSTER",
                "ClusterAsset": {
                    "Appid": 200000000,
                    "AssetName": "openclaw-Test",
                    "ClusterID": "cls-l*****c6",
                    "ClusterName": "openclaw-Test",
                    "ClusterType": "TKE_MANAGED_CLUSTER",
                    "NodeCount": 2,
                    "OnlineNodeCount": 0
                },
                "ErrCode": "",
                "ErrMessage": "",
                "FinishTime": "2026-08-12T03:42:36Z",
                "ID": 2294,
                "Solution": "",
                "StartTime": "2026-08-12T03:42:17Z",
                "Status": "SUCCESS",
                "TaskID": 1389
            }
        ],
        "TotalCount": 5,
        "RequestId": "8dc1ad75-cbb5-4d31-87c7-db1f0c25560c"
    }
}
```

