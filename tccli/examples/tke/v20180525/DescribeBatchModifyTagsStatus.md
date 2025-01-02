**Example 1: 查询批量修改标签状态**

查询批量修改标签状态

Input: 

```
tccli tke DescribeBatchModifyTagsStatus --cli-unfold-argument  \
    --ClusterId cls-j3w5ehty
```

Output: 
```
{
    "Response": {
        "FailedResources": [
            {
                "Resource": "qcs::ccs:ap-guangzhou:uin/3356535506:cluster/cls-q505raey",
                "Error": "err"
            }
        ],
        "Status": "failed",
        "SyncSubresource": true,
        "Tags": [
            {
                "Key": "product",
                "Value": "tke"
            }
        ],
        "RequestId": "33483fde-efec-4d3c-8ff6-340d9dbc2d01"
    }
}
```

