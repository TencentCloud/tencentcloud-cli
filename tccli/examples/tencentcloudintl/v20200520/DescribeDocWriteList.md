**Example 1: 依据写写id获取文档信息**

依据写写id获取文档信息

Input: 

```
tccli tencentcloudintl DescribeDocWriteList --cli-unfold-argument  \
    --WriteNodeId 182618756708614144 \
    --Lang en
```

Output: 
```
{
    "Response": {
        "Response": {
            "DocWriteData": [
                {
                    "CategoryId": 1237,
                    "DocUrl": "https://www.tencentcloud.com/document/product/1237/54319",
                    "Id": 54319,
                    "Lang": "en",
                    "WriteLatestVersion": "182618765651791870",
                    "WriteNodeId": "182618756708614144",
                    "WritePublishedVersion": "182618765651791870"
                }
            ],
            "RequestId": "66fe36e6-fa2b-418f-beea-04a7bac3e196"
        },
        "RequestId": "66fe36e6-fa2b-418f-beea-04a7bac3e196"
    }
}
```

