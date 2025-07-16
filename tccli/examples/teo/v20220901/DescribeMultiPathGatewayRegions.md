**Example 1: 获取可用网关地域列表**

获取站点（ ZoneId 为 zone-27q0p0bal192 ）下，云上网关的可用地域列表。

Input: 

```
tccli teo DescribeMultiPathGatewayRegions --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192
```

Output: 
```
{
    "Response": {
        "GatewayRegions": [
            {
                "RegionId": "ap-beijing",
                "CNName": "北京",
                "ENName": "beijing"
            },
            {
                "RegionId": "ap-shanghai",
                "CNName": "上海",
                "ENName": "shanghai"
            }
        ],
        "RequestId": "a622678d-ea5b-41e8-9cd2-d335816141a0"
    }
}
```

