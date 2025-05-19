**Example 1: 启用跨租户特性**



Input: 

```
tccli tke DescribeMetaFeatureProgress --cli-unfold-argument  \
    --ClusterId cls-adssvfsa
```

Output: 
```
{
    "Response": {
        "Status": "Success",
        "Progress": [
            {
                "Name": "ensureNodeMasterCommunication",
                "StartAt": "2022-07-12-14-23-04",
                "EndAt": "2022-07-12-14-24-04",
                "Status": "Success",
                "Message": "null"
            }
        ],
        "RequestId": "232323-5ed9-4cb7-9194-a95e2cd626e5"
    }
}
```

