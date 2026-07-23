**Example 1: DescribeBlockList**



Input: 

```
tccli cfw DescribeBlockList --cli-unfold-argument  \
    --Direction xx \
    --ByPass xx \
    --Source xx \
    --AssetId xx \
    --Country xx \
    --SearchValue xx \
    --Order xx \
    --StatTimeSpan 0 \
    --Limit 0 \
    --StartTime xx \
    --Offset 0 \
    --EndTime xx \
    --By xx
```

Output: 
```
{
    "Response": {
        "Total": 80,
        "Data": [
            {
                "WhiteTag": "xx",
                "DstAssetId": "xx",
                "Hide": 0,
                "Zone": "xx",
                "Isolate": 0,
                "AssetName": "xx",
                "Direction": 0,
                "SrcVpc": "xx",
                "MaxDate": "xx",
                "LogSource": "xx",
                "IsTop": 0,
                "DstAssetName": "xx",
                "SrcIP": "xx",
                "ByPass": 0,
                "Count": 0,
                "AvgCount": 0.0,
                "EdgeId": "xx",
                "AssetId": "xx",
                "Country": "xx",
                "Ignore": 0,
                "UniqueId": "xx",
                "AppID": "xx",
                "DstVpcName": "xx",
                "SrcVpcName": "xx",
                "Block": 0,
                "DstVpc": "xx",
                "DstIP": "xx",
                "EdgeName": "xx",
                "BlockSource": 0,
                "DstPort": "xx",
                "MinDate": "xx"
            }
        ],
        "TopCount": 0,
        "TopData": [
            {
                "WhiteTag": "xx",
                "DstAssetId": "xx",
                "Hide": 0,
                "Zone": "xx",
                "Isolate": 0,
                "AssetName": "xx",
                "Direction": 0,
                "SrcVpc": "xx",
                "MaxDate": "xx",
                "LogSource": "xx",
                "IsTop": 0,
                "DstAssetName": "xx",
                "SrcIP": "xx",
                "ByPass": 0,
                "Count": 0,
                "AvgCount": 0.0,
                "EdgeId": "xx",
                "AssetId": "xx",
                "Country": "xx",
                "Ignore": 0,
                "UniqueId": "xx",
                "AppID": "xx",
                "DstVpcName": "xx",
                "SrcVpcName": "xx",
                "Block": 0,
                "DstVpc": "xx",
                "DstIP": "xx",
                "EdgeName": "xx",
                "BlockSource": 0,
                "DstPort": "xx",
                "MinDate": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

