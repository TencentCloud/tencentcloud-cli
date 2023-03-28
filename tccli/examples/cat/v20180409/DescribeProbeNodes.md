**Example 1: 查询拨测节点**

查询拨测节点


Input: 

```
tccli cat DescribeProbeNodes --cli-unfold-argument  \
    --NodeType 0 \
    --Location 0 \
    --IsIPv6 True \
    --NodeName 广东 \
    --PayMode 0
```

Output: 
```
{
    "Response": {
        "NodeSet": [
            {
                "Name": "北京-北京市-中国电信[IDC]",
                "Code": "10000",
                "Type": 1,
                "NetService": "中国电信",
                "District": "北京",
                "City": "北京市",
                "IPType": 1,
                "Location": 1,
                "CodeType": "",
                "NodeDefineStatus": 1
            }
        ],
        "RequestId": "avb"
    }
}
```

