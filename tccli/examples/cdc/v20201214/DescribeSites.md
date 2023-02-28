**Example 1: 查询站点列表**

查询站点列表

Input: 

```
tccli cdc DescribeSites --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "SiteSet": [
            {
                "SiteId": "site-98dj3kd",
                "Name": "my-site",
                "Description": "my first site",
                "CreateTime": "2020-12-25T08:39:57Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "60f56861-42af-4778-96c2-018d35141a7f"
    }
}
```

