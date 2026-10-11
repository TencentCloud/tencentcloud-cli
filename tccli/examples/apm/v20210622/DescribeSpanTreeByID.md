**Example 1: 查询trace详情接口信息**

查询trace详情接口信息示例

Input: 

```
tccli apm DescribeSpanTreeByID --cli-unfold-argument  \
    --InstanceId apm-059oXBfTL \
    --Filters.0.Type = \
    --Filters.0.Key traceID \
    --Filters.0.Value 97984ab4e9053954277fe0b34064fbe4 \
    --StartTime 1734847016 \
    --EndTime 1734933416
```

Output: 
```
{
    "Response": {
        "RequestId": "363b22b9-cf43-4a31-bf51-436a1266f4d6",
        "SpanTreeView": {
            "ChartData": {
                "Series": [
                    {
                        "Data": [
                            0,
                            170
                        ],
                        "Name": "startTime",
                        "Stack": "series"
                    },
                    {
                        "Data": [
                            3000643,
                            3000303
                        ],
                        "Name": "timeConsuming",
                        "Stack": "series"
                    }
                ],
                "YAxis": [
                    {
                        "Data": [
                            ""
                        ],
                        "Keys": [
                            ""
                        ]
                    }
                ]
            },
            "CntExceeded": false,
            "CompressedTreeData": "H4sIAAAAAAAA/8RWzW7cNhB+FYOnFpBo6nclXe0gXSRtiuyil8AwKGlWZlYiCYpa2zB8KPoKPbWnAj301h5678u0aR+jEHedpXYV23Gc5LZcfpz55uPwG726QtNjlCGfemEOeRr5RQlRtEAOOhJcA9coQ0K7r+mKukKVoNwW1IoVcHAohezk4RUrr5GDZut/v6ENvOsEctALCYpqJvgGN4wxp/l3DM5blL266hfP4BJliPGVWMJ6+xlcbk7+98cP//74m/m3Wh9YGvSZ1hI3oM9EiRy0onXXo58+maNrZ4BpNdVde1qIEiygTwi6Pumhb/N/LRQczCTlB1O+EKox/HfpvPn5z39+/alH/f3XL2++/32fWCEaKXgv6DabFk1BtcVsoxRmvNWUFzYzj+CE4ABPUguvFS1gemzB0kmahDQPISVRkEahP5ksgORBSOJwkUNoJ5OU4yXjtlA9AVAWSAIovGB1DTbsQVG2bTAWZlP5/WQSnRoE4l1d2/u0kTUorC+ljVJUQ80aphmvLDQHjQ1BJvf0DnGUjEGlUDbDIPZi38KNRNq5OdODSnTaJmg/hy1U3DwaC/nVfP7twbCrb4qWVNFmkJ5gYuEaaFta2WldO5liFeN4LOc4O1PImWj1XsV+FODEy9KAePdr8bVlSOAaamhAq0tX03O3EcXSlUq8hkK7JEqFG+flokzysojdZeuHqy+2En+5S01TVYHeL2PAaesFpxcXOzKfGk8YuTisYK8RxzWiFXCNV6DaoaLDWj3sxa5P/IAkAfEmuzm7FtSpiWRFKDpVH06wnw6uuL8OzHtn+njirjU7GtgnGWwrPWc2BW8ShGkQhF4QeZMtEnj5Dlw8wNWUVx2t4MmFVnSnsN6zTxx0dMbqUgE3tmvmWhymJPEg9SGJ40UI95hrL/rVU+D9A4AerERt3lV/sw+edHdFHZ99jzR7HtKztxjB7bU8Ytt/gjb+kPrGRh/jGhSn9edxvLsG4+3ef9sMbqVivHLPIW9Wxftr8D4hP+yj5g5b+oR38XkdsL95B82MHCgjDnrOOKDM9Rw0bfumpozPNC2WZtP82j183G2eRhYQQgISbHCzt5WZuKKardsuQ8gsX0JlTvXLafsSaqqhfC6qG/hcSFYYe17jZ6DNx+DJo/KNw4/O938AAAD//wEAAP//E/t39j4NAAA=",
            "QueryTimeout": false,
            "TraceOverview": {
                "Duration": 3000643,
                "ErrorMsg": "nil",
                "Operation": "/popup/{id}",
                "ServiceName": "ot-java-order-service",
                "Status": 0,
                "TraceID": "97984ab4e9053954277fe0b34064fbe4"
            },
            "TreeData": ""
        }
    }
}
```

