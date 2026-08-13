**Example 1: 查询已修复漏洞的主机修复详情**



Input: 

```
tccli csip DescribeVulFixedHostDetail --cli-unfold-argument  \
    --VulId 10001 \
    --InstanceId ins-5ijxpaa6 \
    --Offset 0 \
    --Limit 10 \
    --MemberId mem-tencent-6f5******f*6*429
```

Output: 
```
{
    "Response": {
        "VulName": "OpenSSL 远程代码执行漏洞",
        "CveId": "CVE-2024-0727",
        "VulCategory": "LINUX",
        "FixTime": "2025-08-30T23:00:00+08:00",
        "InstanceId": "ins-5ijxpaa6",
        "MachineName": "yuyinghan的主机",
        "PublicIp": "118.24.71.134",
        "PrivateIp": "172.27.0.139",
        "ComponentDetails": [
            {
                "Name": "expat",
                "Version": "2.2.0-12.el7",
                "Path": "/usr/include/zconf.h, /usr/include/zlib.h",
                "FixCommand": "sudo yum update expat"
            }
        ],
        "TotalCount": 49,
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

