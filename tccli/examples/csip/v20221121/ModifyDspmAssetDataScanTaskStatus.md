**Example 1: 暂停、继续、终止Dspm资产数据识别扫描任务**



Input: 

```
tccli csip ModifyDspmAssetDataScanTaskStatus --cli-unfold-argument  \
    --TaskIds 358 \
    --Status 5 \
    --MemberId mem-12e1w1ed
```

Output: 
```
{
    "Response": {
        "DataSet": [
            {
                "Status": 3,
                "TaskId": 358
            }
        ],
        "RequestId": "369fbf75-d652-4d49-a02d-a6a520862aaa"
    }
}
```

