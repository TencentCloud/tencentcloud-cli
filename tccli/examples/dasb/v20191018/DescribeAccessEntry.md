**Example 1: 查询运维人员WEB访问入口**

查询运维人员WEB访问入口

Input: 

```
tccli dasb DescribeAccessEntry --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AccessEntrySet": [
            "https://jr.bh.cloud.tencent.com/login.html?appTag="
        ],
        "IntranetAccessEntry": "https://192.1.0.0/login.html",
        "IntranetAccessStatus": 1,
        "RequestId": "tv5b7oic-y5ji-5py4-gj76-cmnz71119x1o"
    }
}
```

