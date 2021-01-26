**Example 1: 网络攻击日志详情**

网络攻击日志详情

Input: 

```
tccli cwp DescribeAttackLogInfo --cli-unfold-argument  \
    --Id 1023
```

Output: 
```
{
    "Response": {
        "Id": "2012",
        "Quuid": "9e21f60b-0a3d-4406-898b-534e316e025a",
        "SrcPort": 54326,
        "SrcIp": "117.20.113.126",
        "DstPort": 555,
        "DstIp": "106.52.130.63",
        "HttpMethod": "POST",
        "HttpHost": "haoliao55.com:555",
        "HttpContent": "{\"action\":\"im.cts.sync\",\"body\":{\"@type\":\"type.googleapis.com/site.ImCtsSyncRequest\",\"u2Count\":200,\"groupCount\":200},\"header\":{\"_3\":\"1a69c29e-55b5-4298-8a64-4e8bdebe3e13\",\"_4\":\"http://haoliao55.com:555/index.php\",\"_8\":\"1\",\"_6\":\"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0\"},\"packageId\":306280}",
        "HttpHead": "POST /index.php?action=im.cts.sync&body_format=json&lang=1 HTTP/1.1\nHost: haoliao55.com:555\nConnection: keep-alive\nContent-Length: 377\nAccept: */*\nOrigin: http://haoliao55.com:555\nX-Requested-With: XMLHttpRequest\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0\nContent-Type: application/x-www-form-urlencoded; charset=UTF-8\nReferer: http://haoliao55.com:555/index.php?action=page.index\nAccept-Encoding: gzip, deflate\nAccept-Language: zh-CN,zh;q=0.8\nCookie: duckchat_sessionid=LCHSNwfyK5UAAKIbJNk2ZW1IcPevVqO3zTNMi3n3kjOAGorlJ3f5GnquBc2m1J2N; duckchat_page_url=http://haoliao55.com:555?page=groupMsg&x=iu4fs8thai; zaly_site_user=1a69c29e-55b5-4298-8a64-4e8bdebe3e13\n\n",
        "HttpUserAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0",
        "HttpReferer": "http://haoliao55.com:555/index.php?action=page.index",
        "VulType": "fastjson",
        "HttpCgi": "/index.php",
        "HttpParam": "action=im.cts.sync&body_format=json&lang=1",
        "CreatedAt": "2019-07-16 15:43:38",
        "RequestId": "b12a5e5a-9393-453f-a4d9-b42de0b2bcec"
    }
}
```

