**Example 1: Viewing policy list**



Input: 

```
tccli cam ListPolicies --cli-unfold-argument  \
    --Rp 1 \
    --Page 10
```

Output: 
```
{
    "Response": {
        "ServiceTypeList": [],
        "List": [
            {
                "PolicyId": 16313162,
                "PolicyName": "QcloudAccessForCDNRole",
                "AddTime": "2019-04-19 10:55:31",
                "Type": 2,
                "Description": "Tencent Cloud Content Delivery Network (CDN) permissions include CRUD operations for CLS logsets and log topics as well as searching for, downloading, and uploading logs.",
                "CreateMode": 2,
                "Attachments": 0,
                "ServiceType": "cooperator",
                "IsAttached": 1,
                "Deactived": 1,
                "DeactivedDetail": [
                    "cvm"
                ],
                "IsServiceLinkedPolicy": 1
            }
        ],
        "TotalNum": 239,
        "RequestId": "ae2bd2b7-1d55-4b0a-8154-e02407a2b390"
    }
}
```

