**Example 1: 获取资产标签属性**



Input: 

```
tccli csip DescribeAssetTagAttributes --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AssetTypeList": [
            {
                "Text": "腾讯云-云服务器",
                "Value": "tencent-cvm_instance"
            }
        ],
        "ColorOptions": [
            {
                "Text": "蓝色",
                "Value": "blue"
            }
        ],
        "FilterConditions": [
            {
                "Text": "等于",
                "Value": "equals"
            }
        ],
        "TagKeyList": [
            {
                "Text": "Default",
                "Value": "Default"
            }
        ],
        "TagTree": [
            {
                "Children": [
                    {
                        "Color": "red",
                        "Key": "核心",
                        "Value": "1"
                    }
                ],
                "Color": "",
                "Key": "核心",
                "Value": "核心"
            }
        ],
        "TaggingAttributes": [
            {
                "Text": "资产名称",
                "Value": "asset_name"
            }
        ],
        "RequestId": "1a3feac8-d7ef-445c-b9bd-c4856353c92d"
    }
}
```

