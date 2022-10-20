**Example 1: 严重&高危的漏洞趋势**



Input: 

```
tccli tcss DescribeVulTendency --cli-unfold-argument  \
    --EndTime 2020-09-22 \
    --StartTime 2020-09-22 \
    --SphereOfInfluence LATEST
```

Output: 
```
{
    "Response": {
        "VulTendencySet": [
            {
                "VulSet": [
                    {
                        "Cnt": 1,
                        "CurTime": "2020-09-22"
                    }
                ],
                "ImageType": "Local"
            }
        ],
        "RequestId": "xx"
    }
}
```

