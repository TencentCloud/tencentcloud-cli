**Example 1: 请求示例**



Input: 

```
tccli live DescribeAllStreamPlayInfoList --cli-unfold-argument  \
    --QueryTime '2019-12-12 10:00:00'
```

Output: 
```
{
    "Response": {
        "QueryTime": "2019-12-12 10:00:00",
        "DataInfoList": [
            {
                "Bandwidth": 1.82,
                "Online": 1,
                "PlayDomain": "domain.test1.com",
                "Protocol": "Hls",
                "Rate": 0,
                "Request": 19,
                "StreamName": "test1"
            },
            {
                "Bandwidth": 1.59,
                "Online": 1,
                "PlayDomain": "domain.test2.com",
                "Protocol": "Flv",
                "Rate": 0,
                "Request": 10,
                "StreamName": "test2"
            },
            {
                "Bandwidth": 3.6,
                "Online": 2,
                "PlayDomain": "domain.test3.com",
                "Protocol": "Flv",
                "Rate": 0,
                "Request": 12,
                "StreamName": "test3"
            }
        ],
        "RequestId": "k54e3deb-f318-4147-8a68-3c959642f9ec"
    }
}
```

