**Example 1: DescribeMNPReleasedVersionHistory**



Input: 

```
tccli tcmpp DescribeMNPReleasedVersionHistory --cli-unfold-argument  \
    --MNPId mpjl3td541qppx9k \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "DataList": [
                {
                    "MNPId": "mpjl3td541qppx9k",
                    "MNPVersion": "1.0.320",
                    "MNPVersionId": 2548,
                    "MNPVersionNote": "test",
                    "UpdateTime": "1724019035"
                },
                {
                    "MNPId": "mpjl3td541qppx9k",
                    "MNPVersion": "1.0.319",
                    "MNPVersionId": 2543,
                    "MNPVersionNote": "test",
                    "UpdateTime": "1723932635"
                },
                {
                    "MNPId": "mpjl3td541qppx9k",
                    "MNPVersion": "1.0.318",
                    "MNPVersionId": 2538,
                    "MNPVersionNote": "test",
                    "UpdateTime": "1723846259"
                },
                {
                    "MNPId": "mpjl3td541qppx9k",
                    "MNPVersion": "1.0.317",
                    "MNPVersionId": 2530,
                    "MNPVersionNote": "test",
                    "UpdateTime": "1723809176"
                },
                {
                    "MNPId": "mpjl3td541qppx9k",
                    "MNPVersion": "1.0.316",
                    "MNPVersionId": 2520,
                    "MNPVersionNote": "test",
                    "UpdateTime": "1723759837"
                }
            ],
            "TotalCount": 5
        },
        "RequestId": "9a6ad6c7-796d-47c3-bce0-5658b4f05b1d"
    }
}
```

