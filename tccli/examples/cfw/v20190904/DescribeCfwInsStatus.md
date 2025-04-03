**Example 1: 查询cfw引擎升级状态**



Input: 

```
tccli cfw DescribeCfwInsStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CfwInsStatus": [
            {
                "CfwInsId": "cfwnat-xx",
                "CfwInsName": "nat-out",
                "Region": "ap-guangzhou",
                "FwType": "ew",
                "Status": "Running",
                "EventTime": "2022-09-28 10:57:13",
                "RecoverTime": "2022-10-12 16:58:27"
            }
        ],
        "TotalCount": 0,
        "RequestId": "jijijge"
    }
}
```

