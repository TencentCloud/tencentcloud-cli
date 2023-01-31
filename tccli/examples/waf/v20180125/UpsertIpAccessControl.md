**Example 1: UpsertIpAccessControl**

IP黑白名单Upsert接口

Input: 

```
tccli waf UpsertIpAccessControl --cli-unfold-argument  \
    --Domain test.qcloudwaf.com \
    --Items {"ip":"1.2.3.4","source":"custom","note":"test","action":42,"valid_ts":1650095068} \
    --Edition clb-waf
```

Output: 
```
{
    "Response": {
        "FailedCount": 0,
        "FailedItems": "",
        "RequestId": "fea2e723-002b-40e6-8297-7c54455cb7d6"
    }
}
```

