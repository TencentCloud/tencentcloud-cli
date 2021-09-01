**Example 1: 创建攻击日志下载任务**



Input: 

```
tccli waf CreateAttackDownloadTask --cli-unfold-argument  \
    --FromTime '2019-12-30 00:00:00' \
    --ToTime '2019-12-30 23:59:59' \
    --Domain abc.qcloudwaf.com \
    --Name d0wnload
```

Output: 
```
{
    "Response": {
        "Flow": "XXXX-XXXX-XXXX",
        "RequestId": "xxxx-xxxx-xxxxx"
    }
}
```

