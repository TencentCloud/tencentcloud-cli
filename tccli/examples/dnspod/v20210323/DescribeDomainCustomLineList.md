**Example 1: 获取域名的自定义线路列表**

获取域名的自定义线路列表

Input: 

```
tccli dnspod DescribeDomainCustomLineList --cli-unfold-argument  \
    --Domain dnspod.com
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "LineList": [
            {
                "DomainId": 88692848,
                "Name": "line0",
                "Area": "3.3.3.3-3.3.3.6",
                "UseCount": 1,
                "MaxCount": 5000
            },
            {
                "DomainId": 88692848,
                "Name": "line10",
                "Area": "117.7.7.11-117.7.7.12",
                "UseCount": 1,
                "MaxCount": 5000
            },
            {
                "DomainId": 88692848,
                "Name": "line11",
                "Area": "117.7.7.13-117.7.7.14;117.7.7.15-117.7.7.16",
                "UseCount": 2,
                "MaxCount": 5000
            },
            {
                "DomainId": 88692848,
                "Name": "line12",
                "Area": "117.7.7.17-117.7.7.18",
                "UseCount": 1,
                "MaxCount": 5000
            },
            {
                "DomainId": 88692848,
                "Name": "line13",
                "Area": "117.7.7.19-117.7.7.20",
                "UseCount": 1,
                "MaxCount": 5000
            },
            {
                "DomainId": 88692848,
                "Name": "line2",
                "Area": "43.4.4.4-43.4.4.5;5.5.5.5-5.5.5.7",
                "UseCount": 2,
                "MaxCount": 5000
            },
            {
                "DomainId": 88692848,
                "Name": "line3",
                "Area": "7.7.7.7-7.7.7.9",
                "UseCount": 1,
                "MaxCount": 5000
            },
            {
                "DomainId": 88692848,
                "Name": "line4",
                "Area": "65.6.6.6-65.6.6.7",
                "UseCount": 1,
                "MaxCount": 5000
            },
            {
                "DomainId": 88692848,
                "Name": "line5",
                "Area": "117.7.7.7-117.7.7.8",
                "UseCount": 1,
                "MaxCount": 5000
            },
            {
                "DomainId": 88692848,
                "Name": "line9",
                "Area": "117.7.7.9-117.7.7.10",
                "UseCount": 1,
                "MaxCount": 5000
            }
        ],
        "AvailableCount": 0
    }
}
```

