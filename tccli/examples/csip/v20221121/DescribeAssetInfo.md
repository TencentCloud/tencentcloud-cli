**Example 1: 资产基本信息**



Input: 

```
tccli csip DescribeAssetInfo --cli-unfold-argument  \
    --AssetID ins-holt9ne5 \
    --Provider tencent \
    --AssetType cvm_instance
```

Output: 
```
{
    "Response": {
        "Basic": [
            {
                "Label": "创建时间",
                "Style": {
                    "Color": "",
                    "Type": "",
                    "URL": ""
                },
                "Value": "2024-04-02 09:16:40",
                "ValueCount": 0
            }
        ],
        "Network": [
            {
                "Label": "地域",
                "Style": {
                    "Color": "",
                    "Type": "",
                    "URL": ""
                },
                "Value": "西南地区(成都)",
                "ValueCount": 0
            }
        ],
        "Protection": [
            {
                "Label": "UUID",
                "Style": {
                    "Color": "",
                    "Type": "",
                    "URL": ""
                },
                "Value": "8d21e562-b651-4e23-b5fe-c8041d47fb5a",
                "ValueCount": 0
            }
        ],
        "RequestId": "6d496634-8185-41fb-830a-6ec775fbc091"
    }
}
```

