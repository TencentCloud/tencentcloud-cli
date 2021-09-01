**Example 1: 查询本用户可选的拨测点列表示例**



Input: 

```
tccli cat DescribeAgents --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Agents": [
            {
                "Province": "gd",
                "ProvinceName": "广东",
                "Isp": "cmc",
                "IspName": "移动"
            }
        ],
        "RequestId": "e28305fa-cb67-4fdf-b27f-a9383fca8108"
    }
}
```

