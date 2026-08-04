**Example 1: 查询Agent加速模型列表**



Input: 

```
tccli mpa DescribeAgentAccelerators --cli-unfold-argument  \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "AgentAcceleratorSet": [
            {
                "AgentAcceleratorId": "aat-0003ssc7",
                "CnameDomain": "ga-o87nep3a.tencentcloudga005.com",
                "CreateTime": "2026-04-02 17:33:31",
                "Name": "garendu-test",
                "SiteIds": [
                    "site-00w0tfmu"
                ],
                "Status": "",
                "UpdateTime": "2026-04-02 17:33:35",
                "VpcSet": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "531ced0e-bffa-4ed3-8a39-3426e5e957ec"
    }
}
```

