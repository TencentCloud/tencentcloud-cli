**Example 1: 示例**



Input: 

```
tccli csip DescribeCWPScanIpInfo --cli-unfold-argument  \
    --IP 1
```

Output: 
```
{
    "Response": {
        "Announcement": "此 IP为 云安全中心/漏洞扫描服务 扫描 IP，将定期对您的 IP/域名 进行检测，以 发现端口、漏洞、弱口令等风险，若您发现来自此 IP 的扫描行为，请进行放行或加白...",
        "Bussiness": "腾讯业务扫描、VSSProbe",
        "Characteristic": "腾讯业务扫描、VSSProbe",
        "Demo": "X-Custom-User-Agent: Tencent Cloud VSS PocScan",
        "Describe": "腾讯业务扫描、VSSProbe",
        "ISP": "待填充",
        "IsBelongTencent": true,
        "Location": "待填充",
        "Purpose": "发现端口、漏洞、弱口令等风险",
        "Referer": "https://cloud.tencent.com/document/product/664/98499",
        "Target": "IP/域名",
        "RequestId": "facbf7d6-3c77-4648-a701-8aa9ea7dd2c7"
    }
}
```

