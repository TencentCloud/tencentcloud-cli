**Example 1: 获取账号dspm信息列表**



Input: 

```
tccli csip DescribeUserDspmInfoList --cli-unfold-argument  \
    --MemberId mem-5b28e2760c18f07a
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "List": [
            {
                "AppID": 251237296,
                "AssetNum": 30,
                "IsSelfBuy": 1,
                "IsShared": 2,
                "NickName": "",
                "ShareFromAppID": 251237296,
                "Uin": "700000579945"
            }
        ],
        "SelectedAssetNum": 30,
        "RequestId": "a5f433c4-9bcb-4b6a-8c7b-7ce9bd65e84e"
    }
}
```

