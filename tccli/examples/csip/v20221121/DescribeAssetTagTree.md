**Example 1: 获取资产标签树结构数据**



Input: 

```
tccli csip DescribeAssetTagTree --cli-unfold-argument  \
    --MemberId mem-6wfo123
```

Output: 
```
{
    "Response": {
        "TotalCount": 20,
        "TreeData": [
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
        "RequestId": "d1139d4f-de34-4cce-b330-8da41f272b35"
    }
}
```

